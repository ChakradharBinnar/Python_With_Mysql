import mysql.connector as con

mydb = con.connect(host='localhost', user='root',
                   password='Binnar@123', database='data2')

db_cursor = mydb.cursor()
db_cursor.execute(
    'create table employee(id int, name varchar(100), city varchar(100)) ')
print("table created !")
