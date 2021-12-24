import csv
import os
import sys
import collections
import datetime
comune = sys.argv[1]
abitanti = sys.argv[2]
with open(os.path.join(os.getcwd(), comune.replace(" ", "_") + "_wk.csv"), mode='w') as out_file:
    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(["Data","Comune","Casi da inizio pandemia","Incremento", "Settimana", "Casi/100000"])
    with open(os.path.join(os.getcwd(), comune.replace(" ", "_") + ".csv"), mode='r') as in_file:
        # print(file)
        readCSV = csv.reader(in_file, delimiter=',')
        precValue = 0
        weekData = collections.deque(7*[0], 7)
        for idx, row in enumerate(readCSV, start=0):
            if idx > 0:
                if idx > 1:
                    incremento = int(row[2]) - precValue
                else:
                    incremento = 0
                weekData.append(incremento)
                print(weekData)
                weekSum = sum(weekData)
                print(weekSum)
                cases = round(100000 * weekSum / int(abitanti))
                week = datetime.datetime.strptime(row[0], '%Y%m%d').isocalendar()[1]
                out_writer.writerow([row[0], row[1], int(row[2]), incremento, week + 1, cases])
                precValue = int(row[2])
                
