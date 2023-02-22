import requests
import json
from datetime import datetime

API_KEY = 'bGyRxbwvr8h7MvNW4WJx8NGnoHwhwIL6ylmS8PN0'
CODI_TORREDEMBARRA = "DK"

#definicio del dia per extreure les dades
dia = datetime.today().day
if len(str(dia))<2:
    dia = "0" + str(dia)
mes = datetime.today().month
if len(str(mes))<2:
    mes = "0" + str(mes)
any = datetime.today().year

#exportar codi de totes les variables
url_variables = "https://api.meteo.cat/xema/v1/variables/mesurades/metadades"
response = requests.get(url_variables, headers={"Content-Type": "application/json", "X-Api-Key": API_KEY})
variables_original = json.loads(response.content.decode("utf-8"))

variables = {}
for var in variables_original:
    var_temp ={}
    var_temp["nom"] = var["nom"]  
    var_temp["unitat"] = var["unitat"]  
    variables[var["codi"]] = var_temp


#Crida dades estació
url = 'https://api.meteo.cat/xema/v1/estacions/mesurades/'+ CODI_TORREDEMBARRA + '/' + str(any) + '/'+str(mes)+'/'+str(dia)
response = requests.get(url, headers={"Content-Type": "application/json", "X-Api-Key": API_KEY})
dades_original = json.loads(response.content.decode("utf-8"))
index_variables = {'Temperatura màxima': '40', \
'Temperatura mínima':'42', 
'Velocitat del vent a 10 m (vec.)':'20', 
'Direcció del vent a 10 m (m. u)':'21',
'Temperatura': '32',
'Humitat relativa':'33',
'Pressió atmosfèrica':'34',
'Precipitació': '35',
'Precipitació acumulada':'70',
}

dades_avui = {}
for var in dades_original[0]["variables"]:
    dict_temp = {}
    nom_variable = variables[var["codi"]]["nom"]
    unitat_variable = variables[var["codi"]]["unitat"]
    ultim_valor_variable = list(var["lectures"])[-1]["valor"]
    data_ultim_valor_variable = list(var["lectures"])[-1]["data"]
    dict_temp["data"] = data_ultim_valor_variable
    dict_temp["valor"] = ultim_valor_variable
    dict_temp["unitat"] = unitat_variable
    dades_avui[nom_variable] = dict_temp

output = {}
for var in dades_avui: 
    output[var] = dades_avui[var]["valor"]

print(output)