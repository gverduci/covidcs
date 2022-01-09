import pandas as pd
import os
import sys
import csv
from datetime import datetime

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
                df["Data"] = pd.to_datetime(weeks, infer_datetime_format=True)
            df[comune] = results

plt = df.plot(style=".-", grid="true", x="Data", y=comuni, title="Nuovi casi giornalieri per 100000 ab - media mobile 7gg (" + datetime.now().strftime("%d-%b-%Y %H:%M:%S") + ")", figsize=(16,9))

for l in plt.lines:
    y = l.get_ydata()
    if len(y)>0:
        plt.annotate(f'{y[-1]:.0f}', xy=(1,y[-1]), xycoords=('axes fraction', 'data'), 
                     ha='left', va='center', color=l.get_color())

# Customize the major grid
plt.grid(which='major', linewidth='1', color='black')
# Customize the minor grid
plt.minorticks_on()
xtick = df["Data"]
plt.set_xticks( xtick, minor=True )
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

fig = plt.get_figure()

fig.savefig("plot.png")