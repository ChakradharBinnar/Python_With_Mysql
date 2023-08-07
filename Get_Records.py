import mysql.connector as con

connection = con.connect(host='localhost', user='root',
                         password='Binnar@123', database='data2')

db_cursor = connection.cursor()
db_cursor.execute('select * from employee')


for i in db_cursor.fetchall():
    print(i)
