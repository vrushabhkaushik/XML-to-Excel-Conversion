import openpyxl
import xml.etree.ElementTree as ET
import pandas as pd

# load and parse the file
fname = input('Enter File Name: ')
xmlTree = ET.parse('C:\\Stuff\\'+fname+'.xml')
print('Import successful!')
print('Parsing XML file...')
print("XML file parsed successfully!")

x = []

for ele in xmlTree.findall('./item'):
  l = {}
  for i in ele.getchildren():
    l.update({i.tag:i.text})
    #print(i.tag)
  x.append(l)
#print(x)
print("Creating DataFrame...")
df = pd.DataFrame(x)
print("DataFrame created successfully!")
if(df.to_excel(fname+'.xlsx', sheet_name='sheet1', index='False')):
    print("File Created Successfully!")
