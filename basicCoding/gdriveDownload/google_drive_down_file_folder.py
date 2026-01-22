import io
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define the scopes (Permissions)
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_service():
    creds = None
    # Token file stores access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return build('drive', 'v3', credentials=creds)

def download_folder(folder_id, local_path):
    service = get_service()
    
    # 1. Create the local directory if it doesn't exist
    if not os.path.exists(local_path):
        os.makedirs(local_path)

    # 2. Query for files/folders inside this folder
    query = f"'{folder_id}' in parents and trashed = false"
    results = service.files().list(q=query, fields="files(id, name, mimeType)").execute()
    items = results.get('files', [])

    for item in items:
        item_id = item['id']
        item_name = item['name']
        item_type = item['mimeType']
        
        # Define the local path for this specific item
        file_path = os.path.join(local_path, item_name)

        if item_type == 'application/vnd.google-apps.folder':
            # It's a folder! Recursively call this function
            print(f"Entering folder: {item_name}")
            download_folder(item_id, file_path)
        else:
            # It's a file! Download it
            print(f"Downloading file: {item_name}")
            download_single_file(service, item_id, file_path)

def download_single_file(service, file_id, file_path):
    # Note: Google Docs/Sheets require 'export', regular files use 'get_media'
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(file_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    
    done = False
    while not done:
        status, done = downloader.next_chunk()

# Usage
download_folder('1n4WRcSxXjqwljdc1E6H88QtNuqOgt2yr', './My_Downloaded_Folder')
