#pip install mysql-connection-python
import mysql.connector as con

mydb = con.connect(host='localhost', user='root',
                   password='*******', database='data1')

print(mydb, "Successfully connnection establish !")
