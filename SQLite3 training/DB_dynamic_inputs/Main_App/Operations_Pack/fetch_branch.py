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


def fetch_based_branch(inp_branch):
    conn.execute("select * from participants where branch='"+str(inp_branch)+"' ")