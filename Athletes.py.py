import pandas as pd

# Update this path with the exact path copied from File Explorer
file_path = "C:/Users/DELL/Desktop/Athletes.xlsx.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Display the DataFrame
print(df)


import pandas as pd
import xlsxwriter

# Update this path with the exact path copied from File Explorer
csv_file_path = "C:/Users/DELL/Desktop/Athletes.xlsx.csv"
excel_file_path = "C:/Users/DELL/Desktop/Athletes_Formatted.xlsx"

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Write to an Excel file with formatting
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    # Access the XlsxWriter workbook and worksheet
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # Define a bold format
    bold_format = workbook.add_format({'bold': True})

    # Apply bold format to the first row (header)
    worksheet.set_row(0, None, bold_format)

print(f"Formatted Excel file saved as {excel_file_path}")
