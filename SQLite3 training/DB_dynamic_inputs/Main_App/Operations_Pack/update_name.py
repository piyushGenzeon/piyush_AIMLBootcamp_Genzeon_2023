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


def updName(name,id):
    query="update participants set name = '"+str(name)+"' where g_id="+str(id)+""

    conn.execute(query)

    conn.commit()
    # conn.close()


# def updName(inputs):
#     li=inputs.split(",")
#     li1=int(li[0])
#     li2=str(li[1])
#     conn.execute(f"update participants set name= '{li2}' where g_id='{li1}'" )
#     conn.commit()