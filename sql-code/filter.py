import sqlite3

connection = sqlite3.connect('mydatabase.db')

cursor = connection.cursor()

# getting some data as per our requirements. 

# WHERE, like, in, and, or

# cursor.execute('SELECT * from students WHERE score > ?', (80 ,))


# cursor.execute('SELECT * from students WHERE city = "New York"')

# AND : both of the conditions should be true
# cursor.execute('SELECT * from students WHERE city="New York" AND score > 80')

# OR : one of the conditions should be true
# cursor.execute('SELECT * from students where city="Chicago" or score > 80')

# cursor.execute('SELECT * from students WHERE city IN ("Los Angeles", "New York")')

# get the data where name starts with A

# get the data where name ends with e
cursor.execute('SELECT * from students WHERE name LIKE "%e" ')
rows = cursor.fetchall()

for row in rows:
    print(row)