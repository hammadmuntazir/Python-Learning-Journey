import glob
import pandas as pd
import xml.tree.ElementTree as ET
from datetime import datetime

log_file="log_file.txt"
target_file="transformed_data.csv"

def extract_from_csv(file_to_process):
    dataframe=pd.read_csv(file_to_process)
    return dataframe
def extract_from_json(file_to_process):
    dataframe=pd.read_json(file_to_process,lines=True)
    return dataframe
def extract_from_xml(file_to_process):
    dataframe=pd.DataFrame(columns=["name","height","weight"])
    tree=ET.parse(file_to_process)
    root=tree.getroot()
    for person in root:
        name=person.find('name').text
        height=float(person.find('height').text)
        weight=float(person.find('weight').text)
        dataframe=pd.concat([dataframe,pd.DataFrame([{"name":name,"height":height,"weight":weight}])],ignore_index=True)
        return dataframe
    
def extract():
    extracted_data=pd.DataFrame(columns=['name','height','weight'])
    for csvfile in glob.glob('*.csv'):
        if csvfile !=target_file:
            extracted_data=pd.concat([extracted_data,pd.DataFrame(extract_from_csv(csvfile))],ignore_index=True)
    for jsonfile in glob.glob('*.json'):
        if jsonfile != target_file:
            exectracted_data=pd.concat([extracted_data,pd.DataFrame(extract_from_json(jsonfile))],ignore_index=True)
    for xmlfile in glob.glob('*.xml'):
        if xmlfile != target_file:
            extracted_data = pd.concat([extracted_data,pd.DataFrame(extract_from_xml(xmlfile))],ignore_index=True)
    return extracted_data      

# Transform the data 
def transform(data):
    data['height']=round(data.height*0.0254,2)
    data['weight']=round(data.weight*0.453592,2)
    return data
#  Load the Data
def load(targetfile,transformeddata):
    transformeddata.to_csv(targetfile,index=False)
    

