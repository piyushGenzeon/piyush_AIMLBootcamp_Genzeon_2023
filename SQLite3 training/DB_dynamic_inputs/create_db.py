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

#step 4
'''
create table tablename(colname1 datatype contraints, colname2 datatype contraints....)
constraints -> primary key, not null, check, unique
'''


query='''
create table participants(g_id int primary key, name text not null, branch text not null, study text not null DEFAULT 'Btech')
'''

conn.execute(query)