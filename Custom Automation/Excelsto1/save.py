import pandas as pd
import os

cwd = os.path.abspath('C:/Users/Rafal Jankowski/OneDrive - McKinsey & Company/Desktop/OpsExcel')
move = os.path.abspath('C:/Users/Rafal Jankowski/OneDrive - McKinsey & Company/Desktop/OpsXlsm')
files = os.listdir(cwd)
df = pd.DataFrame()

for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(cwd+"/"+file, "Sheet1"), ignore_index=True)
    else:
        pass

# filter all data
new = df.filter(["FMNO", "First Name", "Last Name", "Sub-practice/Serviceline & Affiliation status", "Region", "Reviewer", "Date of review", "Practice/progress review comments", "ITTL2Comments"])
# remove duplicates
clean = new.drop_duplicates()
# create excel writer object
writer = pd.ExcelWriter('output.xlsx')
# write dataframe to excel
clean.to_excel(writer)
# save the excel
writer.save()
print('DataFrame is written successfully to Excel File.')