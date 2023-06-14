#steps:
'''
1.importing sqlite3
2.create database


5. execute query
'''

import sqlite3

#step2 & 3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)

'''
describe tablname  -  sql
'''

details=conn.execute("pragma table_info(participants)")
print(details)

#traverse the data
for i in details:
    print(i)