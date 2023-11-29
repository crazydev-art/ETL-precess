# ETL-precess-
This script performs data extraction and transformation by combining information from CSV, JSON, and XML files into a Pandas DataFrame. Here's a breakdown of the script:

File Paths:

The script defines three file path variables (pathnam_csv, pathnam_json, pathnam_xml) representing directories containing CSV, JSON, and XML files, respectively.
Data Extraction:

The script uses the glob module to get a list of file paths matching the specified patterns for CSV, JSON, and XML files.
It then initializes an empty Pandas DataFrame (df) with columns named 'name', 'height', and 'weight'.
CSV Extraction:

It loops through the list of CSV files (files_csv), reads each CSV file using pd.read_csv, and appends the data to the DataFrame (df).
JSON Extraction:

It loops through the list of JSON files (files_json), reads each JSON file using pd.read_json, and appends the data to the DataFrame (df).
XML Extraction:

It loops through the list of XML files (files_xml), parses each XML file using xml.etree.ElementTree, extracts the data, and appends it to a list (data_xml).
The list (data_xml) is then converted to a DataFrame (df_xml), and its contents are appended to the main DataFrame (df).
Temporary Storage:

The combined DataFrame (df) is stored in a temporary CSV file (tmpfile).
