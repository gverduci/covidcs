import csv
import os
filename = "eta"
# Getting the current work directory (cwd)
thisdir = os.path.join(os.getcwd(), "data")
with open(os.path.join(os.getcwd(), filename.replace(" ", "_") + ".csv"), mode='w') as out_file:
    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(["Data", "0-18", "19-50", "51-70", ">70", "Non noto"])
    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        f.sort()
        for file in f:
            if file.endswith("_eta.csv"):
                #print(os.path.join(r1, file))
                with open(os.path.join(r, file)) as csvfile:
                    print(file)
                    readCSV = csv.reader(csvfile, delimiter=',')
                    data = file.split("-")[0]
                    f0018 = 0
                    f1950 = 0
                    f5170 = 0
                    f70 = 0
                    fnd = 0
                    row_count = 0
                    for row in readCSV:
                        if row_count > 0:
                            if row[0] == "0-18":
                                f0018 = int(row[1])
                            if row[0] == "19-50":
                                f1950 = int(row[1])
                            if row[0] == "51-70":
                                f5170 = int(row[1])
                            if row[0] == ">70":
                                f70 = int(row[1])
                            if row[0] == "#N/A":
                                fnd = int(row[1])
                        row_count = row_count +1
                    out_writer.writerow([data, f0018, f1950, f5170, f70, fnd])