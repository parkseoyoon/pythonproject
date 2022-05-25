#pip install cx_Oracle
#오라클 db와 연동을 위한 라이브러리 설치
#git 연습용 내용 추가

import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', 'localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("select * from emp where deptno = 10")

#print(cursor)

for item in cursor:
    print(item[1], item[5])

conn.close()
