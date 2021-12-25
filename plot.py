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

plt = df.plot(style=".-", grid="true", x="Data", y=comuni, title="Nuovi casi giornalieri per 100000 ab - media mobile 7gg", figsize=(16,9))

for l in plt.lines:
    y = l.get_ydata()
    if len(y)>0:
        plt.annotate(f'{y[-1]:.0f}', xy=(1,y[-1]), xycoords=('axes fraction', 'data'), 
                     ha='left', va='center', color=l.get_color())

fig = plt.get_figure()
fig.savefig("plot.png")