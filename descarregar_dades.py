import json
import csv  
import requests
from datetime import date, timedelta

#url = 'http://www.meteoguilleries.cat/API/dadesdiariesEstacio/arb/2022/1'
BASE_URL = 'http://www.meteoguilleries.cat/API/dadesdiariesEstacio/arb/'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

for any in range (2017,2023):
    for mes in range(1, 13):
        #determine file
        url = BASE_URL + str(any) + "/" + str(mes)
        
        filename = "dades_json_" + str(any) + "_" + str(mes) +".json"
        with open(filename, 'w', encoding='UTF8') as f:
            r = requests.get(url)
            jsonData = json.loads(r.content)
            json.dump(jsonData[0], f)
            # write the header

        f.close()








