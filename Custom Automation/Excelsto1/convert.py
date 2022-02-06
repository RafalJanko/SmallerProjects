import win32com.client
import os
import glob

cwd = os.path.abspath('C:/Users/Rafal Jankowski/OneDrive - McKinsey & Company/Desktop/OpsExcel')

o = win32com.client.Dispatch("Excel.Application")
o.Visible = False
input_dir = cwd
output_dir = cwd
files = glob.glob(cwd + "/*.xlsm")

for filename in files:
    file = os.path.basename(filename)
    output = output_dir + '/' + file.replace('.xlsm','.xlsx')
    wb = o.Workbooks.Open(filename)
    wb.ActiveSheet.SaveAs(output,51)
    wb.Close(True)

