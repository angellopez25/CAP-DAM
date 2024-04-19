import mysql.connector

conn = mysql.connector.connect(user='root', password='Passw0rd',
                              host='localhost',
                              database='cap-dam')
print("Conectado")
conn.close()