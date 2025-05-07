import sqlite3

# to create database
# to create tables in that database


# we have established connection with our database.
# file with db extension. 
connection = sqlite3.connect('mydatabase.db')

# I want to create tables in mydatabase.db

# cursor : will help us to execute queries in database.

cursor = connection.cursor()

cursor.execute('''

    CREATE TABLE myusers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(30),
    email CHAR(50)          
    )

''')