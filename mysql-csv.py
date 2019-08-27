import mysql.connector
import csv

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '17041993',
    auth_plugin = 'mysql_native_password',
    database = 'tokoonline'
)

kursor = db.cursor()
querydb1 = 'describe users'
kursor.execute(querydb1)
y=kursor.fetchall()
keyx = []
for item in y:
    keyx.append(item[0])
print(keyx)

querydb2 = 'select * from users'
kursor.execute(querydb2)
all_data = kursor.fetchall()
dataCsv = []

for item in all_data:
    temp = {}
    for loop in range (len(item)):
        temp[keyx[loop]] = item[loop]
    dataCsv.append(temp)

with open ('mysql_csv.csv','w',newline='') as x:
    writer = csv.DictWriter(x, fieldnames=dataCsv[0].keys())
    writer.writeheader()
    writer.writerows(dataCsv)