import json
import csv  
import requests
from datetime import date, timedelta

BASE_URL = 'http://www.meteoguilleries.cat/API/dadesdiariesEstacio/arb/'
FILENAME_CSV = "dades_meteo.csv"

HEADER = ["data","temperaturaMit","humitatMit","pressioMit","ventMit","ventGrausMit","plujaMaxIntensitat","plujaAvui","plujaMes","plujaAny","radSolarMax","temperaturaMax","temperaturaMin","humitatMax","humitatDataMax","humitatMin","humitatDataMin","pressioMax","pressioDataMax","pressioMin","pressioDataMin","ventMax","ventDirMax","temperaturaDataMax","temperaturaDataMin","ventDataMax","fuelMit","fuelMax","fuelMin","temperaturaSol10Mit","temperaturaSol10Max","temperaturaSol10Min","temperaturaSolM15Mit","temperaturaSolM15Max","temperaturaSolM15Min","ventDesviacioMit","ventDesviacioMax","ventDesviacioMin"]

with open(FILENAME_CSV, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
f.close()

for any in range (2017,2023):
    for mes in range(1, 13):
        #determine file       
        filename_read = "dades_json_" + str(any) + "_" + str(mes) +".json"
        

        with open(filename_read, 'r', encoding='UTF8') as f:
            data = json.load(f)
        f.close()
        
        with open(FILENAME_CSV, 'a+', newline='') as obj:
            csv_writer = csv.writer(obj)
            for dia in data:
                try:
                    filera = [dia["data"],dia["temperaturaMit"], dia["humitatMit"], dia["pressioMit"], dia["ventMit"], dia["ventGrausMit"], dia["plujaMaxIntensitat"], dia["plujaAvui"], dia["plujaMes"], dia["plujaAny"], dia["radSolarMax"], dia["temperaturaMax"], dia["temperaturaMin"], dia["humitatMax"], dia["humitatDataMax"], dia["humitatMin"], dia["humitatDataMin"], dia["pressioMax"], dia["pressioDataMax"], dia["pressioMin"], dia["pressioDataMin"], dia["ventMax"], dia["ventDirMax"], dia["temperaturaDataMax"], dia["temperaturaDataMin"], dia["ventDataMax"], dia["fuelMit"], dia["fuelMax"], dia["fuelMin"], dia["temperaturaSol10Mit"], dia["temperaturaSol10Max"], dia["temperaturaSol10Min"], dia["temperaturaSolM15Mit"], dia["temperaturaSolM15Max"], dia["temperaturaSolM15Min"], dia["ventDesviacioMit"], dia["ventDesviacioMax"], dia["ventDesviacioMin"]]
                except:
                    lst = [None] * 37
                    filera = [dia["data"]] + lst

                print(filera)           
                # Add contents of list as last row in the csv file
                csv_writer.writerow(filera)
        obj.close()





