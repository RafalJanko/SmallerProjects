import os
import pandas as pd
import glob
import win32com.client as win32

# Find all files in a directory & print file names
cwd = os.path.abspath('PATH TO FILES YOU WOULD LIKE TO JOIN')
move = os.path.abspath('PATH TO THE FOLDER YOU WOULD LIKE TO MOVE THE OUTPUT TO')
files = os.listdir(cwd)
df = pd.DataFrame()
# Print file names in the location
print(files)

# For all "xlsm" files covert them to "xlsx"
for file in files:
    if file.endswith(".xlsm"):
        o = win32.Dispatch("Excel.Application")
        o.Visible = False
        input_dir = cwd
        output_dir = cwd
        files = glob.glob(cwd + "/*.xlsm")

        for filename in files:
            file = os.path.basename(filename)
            output = output_dir + '/' + file.replace('.xlsm', '.xlsx')
            wb = o.Workbooks.Open(filename)
            wb.ActiveSheet.SaveAs(output, 51)
            wb.Close(True)
    else:
        pass

cwd = os.path.abspath('PATH TO FILES YOU WOULD LIKE TO JOIN')
move = os.path.abspath('PATH TO THE FOLDER YOU WOULD LIKE TO MOVE THE OUTPUT TO')
files = os.listdir(cwd)
df = pd.DataFrame()

for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(cwd+"/"+file, "Sheet1"), ignore_index=True)
    else:
        pass

# filter all data
new = df.filter(["NAME CUSTOM COLUMNS YOU WOULD LIKE TO FILTER FROM THE OUTPUT"])
# remove duplicates
clean = new.drop_duplicates()
# create excel writer object
writer = pd.ExcelWriter('output.xlsx')
# write dataframe to excel
clean.to_excel(writer)
# save the excel
writer.save()
print('DataFrame is written successfully to Excel File.')