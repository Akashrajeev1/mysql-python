import mysql.connector


conn = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',database='mysql')
cursor = conn.cursor()
sql='''UPDATE EMPLOYEE SET SALARY = SALARY + 1 WHERE AGE = 22'''

try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

sql = '''SELECT * from EMPLOYEE'''
cursor.execute(sql)
print(cursor.fetchall())
conn.close()
