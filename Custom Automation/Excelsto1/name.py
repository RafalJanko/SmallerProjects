names = ['1Europe-SO.xlsm', 'AsiaX-PDP.xlsm', 'newx.xlsx']

new_names = []
for item in names:
    new = item.replace("xlsm","xlsx")
    new_names.append(new)

print(new_names)





# convert

for file in files:
    if file.endswith(".xlsm"):
        file_name = str(file)
        excel = win32.gencache.EnsureDispatch('Excel.Application')

        # Load the .XLSM file into Excel
        wb = excel.Workbooks.Open(f'C:/Users/Rafal Jankowski/OneDrive - McKinsey & Company/Desktop/OpsExcel/{file}')
        # Save it in .XLSX format to a different filename
        excel.DisplayAlerts = False
        wb.DoNotPromptForConvert = True
        wb.CheckCompatibility = True
        new_name = file_name.replace("xlsm", "xslx")
        wb.SaveAs(cwd+f"/{new_name}", FileFormat=51, ConflictResolution=2)
        excel.Application.Quit()

    else:
        pass