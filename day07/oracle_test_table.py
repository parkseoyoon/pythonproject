import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', 'localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("drop table test")
cursor.execute("create table test(id number(2))")
cursor.execute("insert into test values(01)")
cursor.close()
conn.commit()
conn.close()