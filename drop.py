import mysql.connector


conn = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',database='mysql')
cursor = conn.cursor()
cursor.execute("SHOW Tables")
print(cursor.fetchall())


cursor.execute("DROP TABLE EMPLOYEE")
print("Table dropped...")


print("List of tables after dropping the EMPLOYEE table:")
cursor.execute("SHOW Tables")
print(cursor.fetchall())
conn.close()