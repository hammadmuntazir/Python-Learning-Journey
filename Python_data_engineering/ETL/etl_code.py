import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file="log_file.txt"
transformed_file="transformed_data.csv"

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines=True)
    return dataframe
def extract_from_xml(file_to_process):
    dataframe=pd.DataFrame(columns=["name","height","weight"])
    tree=ET.parse(file_to_process)
    root=tree.getroot()
    for person in root:
        name=person.find('name').text
        height=float(person.find('height').text)
        weight=float(person.find('weight').text)
        dataframe=pd.concat([dataframe,pd.DataFrame([{"name":name,"height":height,"weight":weight}])],
                            ignore_index=True)
    return dataframe

def extract():
    extracted_data=pd.DataFrame(columns=['name','height','weight'])
    for csvfile in glob.glob('*.csv'):
        if csvfile != transformed_file :
            extracted_data=pd.concat([extracted_data,pd.DataFrame(extract_from_csv(csvfile))],ignore_index=True)
    for jsonfile in glob.glob('*.json'):
        if jsonfile != transformed_file:
            extracted_data=pd.concat([extracted_data,pd.DataFrame(extract_from_json(jsonfile))],ignore_index=True)
    for xmlfile in glob.glob('*.xml'):
        if xmlfile != transformed_file:
            extracted_data=pd.concat([extracted_data,pd.DataFrame(extract_from_xml(xmlfile))],
                                     ignore_index=True)
    return extracted_data
# Transform the data
def transform(data):
    data['height']=round(data.height*0.0254,2)
    data['weight']=round(data.weight*0.453592,2)
    return data

#  Load the Data 
def load(targetfile,transformeddata):
    transformeddata.to_csv(targetfile,index=False)

# Log the process
def log(message):
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file,"a") as f:
        f.write(f"{timestamp} - {message} \n")
    
if __name__ == "__main__":
    log("ETL Job Started")
    extracted_data=extract()
    log("Data Extraction Completed \n")
    transformed_data=transform(extracted_data)
    log("Data Transformation Completed \n")
    load(transformed_file,transformed_data)
    log("Data loading Completed \n")
    log("ETL Job Completed \n")