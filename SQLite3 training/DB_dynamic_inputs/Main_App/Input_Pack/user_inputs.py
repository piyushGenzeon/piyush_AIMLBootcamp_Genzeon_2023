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

#Insert data Dynamically
def input_data():
    data={}
    g_id=int(input("Enter G_id: "))
    name=input("Enter Nmae: ")
    branch=input("Enter Branch: ")
    study=input("Enter Study: ")
    data["g_id"] = g_id
    data["name"] = name
    data["branch"] = branch
    data["study"] = study
    conn.execute('''
    insert into participants(G_id,name,branch,study) values(?,?,?,?)
    ''',(data.get('g_id'),data.get('name'),data['branch'],data['study']))

    conn.commit()
    print("Data entered successfully")

