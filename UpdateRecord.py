import mysql.connector as con

connection = con.connect(host='localhost', user='root',
                         password='*******', database='data2')

db_cursor = connection.cursor()
update_que = 'update data2.employee set city=%s where name=%s'
val = ('Akole', 'Chikku')
db_cursor.execute(update_que, val)
connection.commit()
