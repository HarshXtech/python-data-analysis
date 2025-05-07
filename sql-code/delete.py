import sqlite3

# 

connection = sqlite3.connect('mydatabase.db')

cursor = connection.cursor()

# DELETE query

# cursor.execute('DELETE FROM myusers WHERE id=4')

cursor.execute('DELETE FROM myusers')

connection.commit()


# CRUD : create, read, update, delete