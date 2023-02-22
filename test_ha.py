import json
import requests
from datetime import datetime

#logger.info("Script dades meteo llançat...")
#url = 'http://www.meteoguilleries.cat/API/dadesdiariesEstacio/arb/2022/1'
BASE_URL = 'http://www.meteoguilleries.cat/API/dadesdiariesEstacio/arb/'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

dia = datetime.today().day
mes = datetime.today().month
any = datetime.today().year

        determine file
url = BASE_URL + str(any) + "/" + str(mes)

r = requests.get(url)
jsonData = json.loads(r.content)
data=jsonData[0]

#                         - data
                        # - temperaturaMax
                        # - temperaturaMin
                        # - temperaturaMit
                        # - humitatMax
                        # - humitatMin
                        # - humitatMit
                        # - pressioMax
                        # - pressioMin
                        # - pressioMit
                        # - ventMin
                        # - ventMit
                        # - ventGrausMit
                        # - plujaAvui
                        # - plujaMaxIntensitat
                        # - radSolarMax
                        # - ventDirMax
                        # - ventMax


resultat = data[dia-1]["data"]\
+":"+data[dia-1]["temperaturaMax"]\
+":"+data[dia-1]["temperaturaMin"]\
+":"+data[dia-1]["temperaturaMit"]\
+":"+data[dia-1]["humitatMax"]\
+":"+data[dia-1]["humitatMin"]\
+":"+data[dia-1]["humitatMit"]\
+":"+data[dia-1]["pressioMax"]\
+":"+data[dia-1]["pressioMin"]\
+":"+data[dia-1]["pressioMit"]\
+":"+data[dia-1]["ventMin"]\
+":"+data[dia-1]["ventMit"]\
+":"+data[dia-1]["ventGrausMit"]\
+":"+data[dia-1]["plujaAvui"]\
+":"+data[dia-1]["plujaMaxIntensitat"]\
+":"+data[dia-1]["radSolarMax"]\
+":"+data[dia-1]["ventDirMax"]\
+":"+data[dia-1]["ventMax"]\


print (resultat)









