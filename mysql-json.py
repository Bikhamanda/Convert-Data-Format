import mysql.connector
import json

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
keyx = []
for item in kursor.fetchall():
    keyx.append(item[0])

querydb2 = 'select * from users'
kursor.execute(querydb2)
all_data = kursor.fetchall()
dataCsv = []

for item in all_data:
    temp = {}
    for loop in range (len(item)):
        if type(item[loop]) == type({'a'}):
            temp[keyx[loop]] = str(item[loop])[2:-2]
        else:
            temp[keyx[loop]] = item[loop]
    dataCsv.append(temp)

print(dataCsv)

with open ('mysql-json.json','w') as x:
    json.dump(dataCsv, x)