import mysql.connector as con

connection = con.connect(host='localhost', user='root',
                         password='*******', database='data2')

db_cursor = connection.cursor()
delete_que = 'delete from employee where name = %s'
val = ('Pradnya',)
db_cursor.execute(delete_que, val)
connection.commit()
print(db_cursor.rowcount, " Record deleted")
