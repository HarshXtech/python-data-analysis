import sqlite3

connection = sqlite3.connect('mydatabase.db')

cursor = connection.cursor()

# average of total scores

# cursor.execute('SELECT MAX(score) FROM students')


# to count total number of students

# cursor.execute('SELECT COUNT(*) FROM students')


# Group by 

# cursor.execute('SELECT subject, MIN(score) FROM students GROUP BY subject')

cursor.execute('SELECT city, count(*) FROM students GROUP BY city')
rows = cursor.fetchall()

for row in rows:
    print(row)