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
insert into tablename values('','')
'''

query='''insert into participants values(101,'Piyush','CSE','Betech','piyush@gmail.com'),
(102,'Shubham','Civil','Betech','shubham@gmail.com'),
(103,'Swanand','Mech','Betech','swanand@gmail.com'),
(104,'Varad','mech','Betech','varad@gmail.com'),
(105,'Aniket','ETC','Betech','aniket@gmail.com')'''


conn.execute(query)
conn.commit()