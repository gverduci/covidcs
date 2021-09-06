import requests 
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
import time
import os

#my_url = 'https://flo.uri.sh/visualisation/5338483/embed?auto=1'  
my_url = 'https://flo.uri.sh/visualisation/6142681/embed?auto=1'
ret = requests.get(my_url)

page_soup = soup(ret.text, 'lxml')
data = page_soup.find('script').parent.find_all('script')[-1]

jsonColumnsstr = data.text.partition("_Flourish_data_column_names =")[2]
jsonColumnsstr = jsonColumnsstr.partition(",\n")[0]
oJsonColumns = json.loads(jsonColumnsstr)["points"]

jsonstr = data.text.partition("_Flourish_data =")[2]
jsonstr = jsonstr.partition(",\n")[0]
oJson = json.loads(jsonstr)["points"]
numComuni = len(oJson)

resultsHeader = []
results = []
resultsComuneHeader = ["Data",oJsonColumns['lat'], oJsonColumns['lon'], oJsonColumns['metadata'][0], oJsonColumns['metadata'][1], oJsonColumns['name']]
resultsRende = []

print(resultsComuneHeader)

resultsHeader.append([oJsonColumns['lat'], oJsonColumns['lon'], oJsonColumns['metadata'][0], oJsonColumns['metadata'][1], oJsonColumns['name']])
print(resultsHeader)

for comune in oJson:
    results.append([comune['lat'], comune['lon'], comune['metadata'][0], comune['metadata'][1], comune['name']])
    
    if comune['name'] == "RENDE":
        resultsRende.append([time.strftime("%Y%m%d"), comune['lat'], comune['lon'], comune['metadata'][0], comune['metadata'][1], comune['name']])


dirname = os.path.dirname(__file__)

rendefilename = os.path.join(dirname, 'rende_map.csv')
df_rende = pd.DataFrame(resultsRende, columns = resultsComuneHeader)
df_rende_csv = pd.read_csv(rendefilename)
print(df_rende_csv)
resultRende = pd.concat([df_rende_csv, df_rende.reset_index(drop=True)], ignore_index=True)
#df_rende_csv = df_rende_csv.append(df_rende, ignore_index=True,sort=False)
print(resultRende)
print()
df =  pd.DataFrame(results, columns = resultsHeader)
filename = time.strftime("%Y%m%d-%H%M%S") + '_map.csv'
fullfilename = os.path.join(dirname, 'data/' + filename)
df.to_csv(fullfilename, encoding='utf-8', index=False)
# print(df)

# print(df_rende)
resultRende.to_csv(rendefilename, encoding='utf-8', index=False)