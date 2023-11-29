import glob  
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime # for logging and debugging 


tmpfile    = "temp.tmp"               # file used to store all extracted data
logfile    = "logfile.txt"            # all event logs will be stored in this file
targetfile = "transformed_data.csv"   # file where transformed data is stored
coulumn = ['name', 'height', 'weight']

pathnam_csv = "/Users/yassineoc/Desktop/VisualStudio/Coursera/source/*.csv"
pathnam_json = "/Users/yassineoc/Desktop/VisualStudio/Coursera/source/*.json"
pathnam_xml= "/Users/yassineoc/Desktop/VisualStudio/Coursera/source/*.xml"
#----------------------------------------------Extraction code------------------------
coulumn = ['name', 'height', 'weight']
files_csv = glob.glob(pathnam_csv)
files_json = glob.glob(pathnam_json)
files_xml = glob.glob(pathnam_xml)


# Create an empty DataFrame with the specified columns
df = pd.DataFrame(columns=coulumn)

# Loop through CSV files and append them to the DataFrame
for file in files_csv:
    df = pd.concat([df,pd.read_csv(file)], ignore_index=True)

# Loop through json files and append them to the DataFrame
for file in files_json:
    df = pd.concat([df,pd.read_json(file,lines=True)], ignore_index=True)

# Loop through json files and append them to the DataFrame
data_xml =[]
for file in files_xml :
    tree = ET.parse(file)
    root = tree.getroot()
    for element in root:
        row = {}
        for subelement in element:
            row [subelement.tag] = subelement.text
        data_xml.append(row)

df_xml = pd.DataFrame(data_xml)
df = pd.concat([df,df_xml], ignore_index=True)


df.to_csv(tmpfile)


