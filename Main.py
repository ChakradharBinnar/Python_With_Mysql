#pip install mysql-connection-python
import mysql.connector as con

mydb = con.connect(host='localhost', user='root',
                   password='Binnar@123', database='data1')

print(mydb, "Successfully connnection establish !")
