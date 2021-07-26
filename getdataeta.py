import requests 
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
import time
import os

#my_url = 'https://flo.uri.sh/visualisation/4496845/embed?auto=1'  
my_url = 'https://flo.uri.sh/visualisation/6131796/embed?auto=1'

ret = requests.get(my_url)

page_soup = soup(ret.text, 'lxml')
data = page_soup.find('script').parent.find_all('script')[-1]

jsonColumnsstr = data.text.partition("_Flourish_data_column_names =")[2]
jsonColumnsstr = jsonColumnsstr.partition(",\n")[0]
oJsonColumns = json.loads(jsonColumnsstr)["data"]

jsonstr = data.text.partition("_Flourish_data =")[2]
jsonstr = jsonstr.partition(";")[0]
oJson = json.loads(jsonstr)["data"]
numComuni = len(oJson)

resultsHeader = []
results = []

resultsHeader.append([oJsonColumns['label'], oJsonColumns['value'][0], oJsonColumns['value'][1]])
print(resultsHeader)

for comune in oJson:
    results.append([comune['label'], comune['value'][0], comune['value'][1]])

dirname = os.path.dirname(__file__)

df =  pd.DataFrame(results, columns = resultsHeader)
filename = time.strftime("%Y%m%d-%H%M%S") + '_eta.csv'
fullfilename = os.path.join(dirname, 'data/' + filename)
df.to_csv(fullfilename, encoding='utf-8', index=False)
# print(df)