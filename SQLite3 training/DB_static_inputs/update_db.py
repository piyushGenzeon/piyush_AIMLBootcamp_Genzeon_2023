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

query="update participants set name='psendurse' where g_id=1"

conn.execute(query)
conn.commit()
conn.close()