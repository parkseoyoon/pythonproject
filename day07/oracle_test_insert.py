import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', 'localhost:1521/XE')
cursor = conn.cursor()
#sql = "insert into dept values(50, 'database', 'seoul')"
#cursor.execute(sql)
sql = "insert into dept values(:1,:2,:3)"
code = input('부서 코드(2자리 숫자) >>> ')
dname = input('부서명 >>> ')
city = input('위치 >>> ')
data = (int(code), dname, city)
cursor.execute(sql, data)
cursor.close()
conn.commit()
conn.close()

# insert, delete, update, select