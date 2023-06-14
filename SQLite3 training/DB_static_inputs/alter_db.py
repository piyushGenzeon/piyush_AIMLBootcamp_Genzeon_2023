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
Rename column
add new column
change the datatype
remove / add any constraints
'''

'''
add column - mailid
ALTER table table_name add column column_name datatype constraintrs
'''

conn.execute('''
alter table participants add column mail_id text not null
''')