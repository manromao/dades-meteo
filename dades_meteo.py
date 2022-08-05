import json
import csv  
import requests
from datetime import date, timedelta

BASE_URL = 'http://www.meteoguilleries.cat/API/dadesdiariesEstacio/arb/'
FILENAME_CSV = "dades_meteo.csv"

HEADER = ['Data',"pluja"]

with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
f.close()

for any in range (2022,2023):
    for mes in range(3, 9):
        #determine file
        url = BASE_URL + str(any) + "/" + str(mes)
        
        filename_read = "dades_json_" + str(any) + "_" + str(mes) +".json"
        

        with open(filename_read, 'r', encoding='UTF8') as f:
            data = json.load(f)
        f.close()
        print(data[0])
        
        with open(FILENAME_CSV, 'a+', newline='') as obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)
        obj.close()





