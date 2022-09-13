import mysql.connector


conn = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',database='mysql')


cursor = conn.cursor()

cursor.execute("SELECT DATABASE()")


data = cursor.fetchone()
print("Connection established to:",data)


conn.close()