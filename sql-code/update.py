import sqlite3

connection = sqlite3.connect('mydatabase.db')

cursor = connection.cursor()


# update query

# cursor.execute('UPDATE myusers SET name="Rahul" WHERE id=4')

cursor.execute('UPDATE myusers SET email="rahul@gmail.com" WHERE name="Rahul"')

connection.commit()

connection.close()

# cursor.execute('SELECT * from myusers')