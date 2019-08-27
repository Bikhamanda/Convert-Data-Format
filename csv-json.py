import csv
import json

all_data = []
with open ('test.csv','r',newline='') as x:
    reader = csv.DictReader(x)
    for item in reader:
        all_data.append(dict(item))

with open ('csv2json.json','w') as x:
    json.dump(all_data, x)