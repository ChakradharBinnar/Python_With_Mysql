import mysql.connector as con

connection = con.connect(host='localhost', user='root',
                         password='Binnar@123', database='data2')

db_cursor = connection.cursor()
delete_que = 'delete from employee where name = %s'
val = ('Pradnya',)
db_cursor.execute(delete_que, val)
connection.commit()
print(db_cursor.rowcount, " Record deleted")
