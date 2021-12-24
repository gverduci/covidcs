import pandas as pd
import os
import sys
import csv

# for idx, comune in enumerate(sys.argv, start=0):
#     if idx > 0:
#         resultsHeader.append(comune)

df = pd.DataFrame([])
comuni = []

for idx, comune in enumerate(sys.argv, start=0):
    if idx > 0:
        comuni.append(comune)
        weeks = []
        results = []
        with open(os.path.join(os.getcwd(), comune.replace(" ", "_") + "_wk.csv"), mode='r') as in_file:
            readCSV = csv.reader(in_file, delimiter=',')
            for idx2, row in enumerate(readCSV, start=0):
                if idx2 > 0:
                    if idx == 1:
                        weeks.append(row[0])
                    results.append(int(row[5]))
            if idx == 1:
                df["Data"] = weeks
            df[comune] = results

plt = df.plot(x="Data", y=comuni, title="Casi/100000 x settimana", figsize=(12,8))
fig = plt.get_figure()
fig.savefig("plot.png")