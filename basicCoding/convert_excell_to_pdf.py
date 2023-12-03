# Import Module
from win32com import client
  
# Open Microsoft Excel
excel = client.Dispatch("Excel.Application")
  
# Read Excel File
sheets = excel.Workbooks.Open('C:/Users/FeCa1/Downloads/Prüfprotokoll_M05s_IBMUCP_SP51_BF1.xlsx')
work_sheets = sheets.Worksheets[0]
  
# Convert into PDF File
work_sheets.ExportAsFixedFormat(0, 'C:/Users/FeCa1/Downloads/Prüfprotokoll_M05s_IBMUCP_SP51_BF1.pdf')