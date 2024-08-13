# Athletes2024


This project demonstrates how to process and format data from an Excel file using Python. Specifically, it takes a CSV file containing athlete information, converts it to an Excel file, and then formats the first row of the Excel file to have bold text and centered alignment.

Athletes Data Analysis
Project Overview
This project involves processing and formatting athlete data from a CSV file. The goal was to load the data, apply formatting to make the first row bold and save the results into a new Excel file.

Initial Problem Statement
You had a dataset containing information about athletes in a CSV file. The requirements were to:

Load the CSV file.
Format the first row of the data to be bold.
Save the formatted data into a new Excel file.
Files Included:

Athletes.py: Python script for processing and formatting the data.
Athletes.xlsx.csv: Original dataset in CSV format.
Athletes_Formatted.xlsx: Final result with the first row formatted.

Libraries Used
Pandas: A powerful data manipulation library.
openpyxl: A library used for reading and writing Excel files.
xlsxwriter: A library used for advanced Excel file formatting.


Create and Activate a Virtual Environment:

python -m venv .venv
.\.venv\Scripts\activate


Install Required Libraries:

pip install pandas openpyxl xlsxwriter
Code Explanation
Athletes.py

This script performs the following steps:

Imports Libraries:

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font


Loads Data from CSV:

file_path = "C:/Users/DELL/Desktop/Athletes.xlsx.csv"
df = pd.read_csv(file_path)


Writes Data to Excel and Formats the First Row:

output_path = "C:/Users/DELL/Desktop/Athletes_Formatted.xlsx"
df.to_excel(output_path, index=False, engine='xlsxwriter')

import xlsxwriter

workbook = xlsxwriter.Workbook(output_path)
worksheet = workbook.add_worksheet()

bold_format = workbook.add_format({'bold': True})
worksheet.set_row(0, None, bold_format)


Saves the Formatted Excel File:
workbook.close()

Troubleshooting
ModuleNotFoundError: Ensure that all required libraries are installed in your virtual environment.
FileNotFoundError: Verify that the file paths specified in the script are correct and that the files exist in those locations.
Contributing

