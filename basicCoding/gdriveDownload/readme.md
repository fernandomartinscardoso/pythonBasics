## Downloading file from Google Drive using Python

Downloading files from Google Drive using Python is typically done using the **Google Client Library**. This is the most secure and official method, though it requires a bit of initial setup in the Google Cloud Console.

### 1. Prerequisites

Before writing code, you need to set up your access:

1. **Create a Project:** Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. **Enable the API:** Search for and enable the **Google Drive API**.
3. **Create Credentials:** Create an **OAuth 2.0 Client ID** (for personal apps) or a **Service Account** (for automated server scripts). Download the JSON file and rename it `credentials.json`.
4. **Install Libraries:**
```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

```

---

### 2. The Python Script

The following script handles authentication and downloads a file by its **File ID** (found in the file's URL).

```python
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

def download_file(file_id, output_filename):
    service = get_service()
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(output_filename, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")

# Usage
download_file('YOUR_FILE_ID_HERE', 'downloaded_image.png')

```

---

### 3. Alternative: Using `gdown` (For Public/Shared Files)

If the file is public or you have a direct share link, the `gdown` library is much simpler and doesn't require the full API setup.

1. **Install:** `pip install gdown`
2. **Code:**
```python
import gdown

url = 'https://drive.google.com/uc?id=YOUR_FILE_ID'
output = 'my_file.zip'
gdown.download(url, output, quiet=False)

```



---

### Summary of Approaches

| Method | Best For | Pros | Cons |
| --- | --- | --- | --- |
| **Official API** | Private files / Production apps | Secure, full control, handles large files | Complex setup (OAuth) |
| **`gdown` Library** | Public or Shared links | Very easy to use | Not suitable for high-security environments |
| **`requests`** | Simple public downloads | No extra libraries needed | Fails on large files due to virus scan warnings |

## Adapting project to download folders

Downloading a folder is slightly more complex than downloading a single file because the Google Drive API does not provide a single "Download Folder" button. Instead, you must **recursively** list the contents of the folder and download each item individually while recreating the directory structure on your local machine.

### 1. Updated Script logic

To download a folder, we need to:

1. **Identify if the ID is a folder:** Check the MIME type.
2. **List files:** Query for all items where the `parents` attribute matches your Folder ID.
3. **Handle sub-folders:** If a child is also a folder, the function should call itself (recursion).

### 2. The Python Implementation

This script extends the previous official API method.

```python
import io
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
# ... (Include the authentication logic 'get_service' from the previous message)

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
# download_folder('YOUR_FOLDER_ID_HERE', './My_Downloaded_Folder')

```

---

### 3. Key Considerations

* **Google Workspace Files:** If your folder contains Google Docs, Sheets, or Slides, `get_media` will fail. You must use `service.files().export()` and specify a MIME type (like PDF or Office) for those specific files.
* **Rate Limits:** If you are downloading thousands of files, you may hit API rate limits. Adding a small `time.sleep()` between downloads can help.
* **Duplicate Names:** Google Drive allows multiple files to have the same name in the same folder. Your local OS likely does not. You might want to add a check to rename files if `os.path.exists(file_path)` is true.

### 4. Simpler Alternative: `gdown`

If you prefer the command line or a simpler script, the `gdown` library supports folders natively:

```bash
pip install gdown
gdown --folder https://drive.google.com/drive/folders/YOUR_FOLDER_ID

```

