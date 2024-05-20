import pandas as pd

# Load the Excel file
df = pd.read_excel('data_mystery_data.xlsx')
"""
for index, row in df.iterrows():
    temp = row['Ankomstdatum'].split('/')
    
    print(row['Ankomstdatum'])
"""

df['Ankomstdatum'] = pd.to_datetime(df['Ankomstdatum'], format='%m/%d/%Y')
df['Ankomstdatum'] = df['Ankomstdatum']
# Save the DataFrame back to an Excel file
df.to_excel('data2.xlsx', index=False)
print("done")