import csv
import os
import sys
comune = sys.argv[1]
# Getting the current work directory (cwd)
thisdir = os.path.join(os.getcwd(), "data")
with open(os.path.join(os.getcwd(), comune.replace(" ", "_") + ".csv"), mode='w') as out_file:
    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(["Data","Comune","Casi da inizio pandemia","Deceduti da inizio pandemia","Attuali ricoverati in rianimazione","Attuali ricoverati altri reparti","In isolamento domiciliare ultimi 30gg"])
    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        f.sort()
        for file in f:
            if not(file.endswith("_map.csv")):
                #print(os.path.join(r1, file))
                with open(os.path.join(r, file)) as csvfile:
                    print(file)
                    readCSV = csv.reader(csvfile, delimiter=',')
                    for row in readCSV:
                        if row[0] == comune:
                            out_writer.writerow([file.split("-")[0]] + row)