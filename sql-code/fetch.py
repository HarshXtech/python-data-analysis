import sqlite3

connection = sqlite3.connect('mydatabase.db')

cursor = connection.cursor()

# to fetch the data from table

# cursor.execute('SELECT * FROM myusers')

cursor.execute('SELECT * FROM myusers where name="Harsh"')
# rows = cursor.fetchall()

data = cursor.fetchone()

print(data)


# for row in rows:
#     print(row)