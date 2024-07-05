import mysql.connector
from utilities.configurations import *
#conn = mysql.connector.connect(host='localhost',database= 'PythonAutomation4', user = 'root',password='kunaltalwar')

conn = getConnection()
print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
'''
row = cursor.fetchone()
print(row, row[3])
row = cursor.fetchone()
rowAll = cursor.fetchall()
print(rowAll)
'''
rows = cursor.fetchall()
print(type(rows), rows)
sum = 0
for row in rows:
    print(row[2])
    sum = sum + row[2]
print(sum)
assert sum == 361

query = "update customerInfo set Location = %s where Coursename = %s"
data = ("UK", "Jmeter")
cursor.execute(query, data)
conn.commit()
conn.close()