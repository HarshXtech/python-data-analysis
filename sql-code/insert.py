import sqlite3

# 

connection = sqlite3.connect('mydatabase.db')

cursor = connection.cursor()


# to insert data in my users table!

# cursor.execute('INSERT INTO myusers (name, email) VALUES (?, ?)', ("Dhaval", "dhaval@gmail.com"))

# data = [
#     ("John", 'john@gmail.com'),
#     ('don', 'don@gmail.com'),
#     ('ron', 'ron@gmail.com'),
# ]

# cursor.executemany('INSERT INTO myusers (name, email) VALUES (?, ?)', data)
connection.commit()