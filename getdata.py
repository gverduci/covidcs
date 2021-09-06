import requests 
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
import time
import os

#my_url = 'https://flo.uri.sh/visualisation/4523774/embed?auto=1'  
my_url = 'https://flo.uri.sh/visualisation/6131807/embed?auto=1'

ret = requests.get(my_url)

page_soup = soup(ret.text, 'lxml')
data = page_soup.find('script').parent.find_all('script')[-1]

jsonColumnsstr = data.text.partition("_Flourish_data_column_names =")[2]
jsonColumnsstr = jsonColumnsstr.partition(",\n")[0]
oJsonColumns = json.loads(jsonColumnsstr)["rows"]

jsonstr = data.text.partition("_Flourish_data =")[2]
jsonstr = jsonstr.partition(",\n")[0]
oJson = json.loads(jsonstr)["rows"]
numComuni = len(oJson)

resultsHeader = []
results = []
resultsComuneHeader = ["Data",oJsonColumns['columns'][0], oJsonColumns['columns'][1], oJsonColumns['columns'][2], oJsonColumns['columns'][3], oJsonColumns['columns'][4], oJsonColumns['columns'][5]]
resultsRende = []

resultsHeader.append([oJsonColumns['columns'][0], oJsonColumns['columns'][1], oJsonColumns['columns'][2], oJsonColumns['columns'][3], oJsonColumns['columns'][4], oJsonColumns['columns'][5]])

for comune in oJson:
    results.append([comune['columns'][0], comune['columns'][1], comune['columns'][2], comune['columns'][3], comune['columns'][4], comune['columns'][5]])
    
    if comune['columns'][0] == "RENDE":
        resultsRende.append([time.strftime("%Y%m%d"), comune['columns'][0], comune['columns'][1], comune['columns'][2], comune['columns'][3], comune['columns'][4], comune['columns'][5]])


dirname = os.path.dirname(__file__)

rendefilename = os.path.join(dirname, 'rende.csv')
df_rende = pd.DataFrame(resultsRende, columns = resultsComuneHeader)
df_rende_csv = pd.read_csv(rendefilename)
resultRende = pd.concat([df_rende_csv, df_rende.reset_index(drop=True)], ignore_index=True)
#df_rende_csv = df_rende_csv.append(df_rende, ignore_index=True,sort=False)
print(resultRende)
print()
df =  pd.DataFrame(results, columns = resultsHeader)
filename = time.strftime("%Y%m%d-%H%M%S") + '.csv'
fullfilename = os.path.join(dirname, 'data/' + filename)
df.to_csv(fullfilename, encoding='utf-8', index=False)
# print(df)

# print(df_rende)
resultRende.to_csv(rendefilename, encoding='utf-8', index=False)