import sqlite3

connection = sqlite3.connect('mydatabase.db')

cursor = connection.cursor()

# cursor.execute('SELECT * FROM students ORDER BY score DESC')

# we can sort data in either numerical or alphabetical way

# cursor.execute('SELECT * FROM students ORDER BY name DESC')

# apply sorting to multiple columns!

rows = cursor.fetchall()

for row in rows:
    print(row)