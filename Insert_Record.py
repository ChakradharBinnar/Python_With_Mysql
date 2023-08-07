import mysql.connector as con

connection = con.connect(host='localhost', user='root',
                         password='Binnar@123', database='data2')

db_cursor = connection.cursor()

# single record inserted
# insert_query = db_cursor.execute(
#     'insert into employee(id, name, city) values (%s,%s,%s)', db_list=(4, 'swara', 'nashik'))


# multiple record inseted
insert_query = 'insert into employee(id, name, city) values (%s,%s,%s)'

db_list = [(2, 'swara', 'Delhi'), (3, 'Pradnya', 'sangamner')]

db_cursor.executemany(insert_query, db_list)
connection.commit()

print(db_cursor.rowcount, "record inserted successfully !")
