import csv
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '17041993',
    database = 'tokoonline',
    auth_plugin = 'mysql_native_password'
)
kursor = db.cursor()

all_data = []
with open ('test.csv','r',newline='') as x:
    reader = csv.DictReader(x)
    for item in reader:
        all_data.append(dict(item))

keyx = []
for key in all_data[0].keys():
    keyx.append(key)

kursor.execute(('create table users1 ({} varchar(100))').format(keyx[0]))

for loop in range (len(keyx)-1):
    kursor.execute('''alter table users
add column 
{} varchar(100)'''.format(keyx[loop+1]))
    db.commit()

keyx = []
valx = []
for item in all_data:
    k = []
    v = []
    for key,val in item.items():
        k.append(key)
        v.append(val)
    keyx.append(k)
    valx.append(v)

for key,val in zip(keyx,valx):
    kursor.execute('insert into users1 {} values {}'.format(str(tuple(key)).replace("'",''),str(tuple(val)).replace("{'",'').replace("'}",'')))
    db.commit()