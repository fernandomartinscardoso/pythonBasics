import win32com.client
import os

path1="first_presentation.pptx"  
path2="second_presentation.pptx"    
#path3="third_presentation.pptx" 
# Add as many paths as required, and include in the lst below

lst=[path1,path2]
output_path="merged_presentations.pptx" 

def merge_presentations(presentations, path):
  ppt_instance = win32com.client.Dispatch('PowerPoint.Application')
  prs = ppt_instance.Presentations.open(os.path.abspath(presentations[0]), True, False, False)

  for i in range(1, len(presentations)):
      prs.Slides.InsertFromFile(os.path.abspath(presentations[i]), prs.Slides.Count)

  prs.SaveAs(os.path.abspath(path))
  prs.Close()

merge_presentations(lst,output_path)