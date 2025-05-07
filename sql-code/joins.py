import sqlite3

connection = sqlite3.connect('mydatabase.db')

cursor = connection.cursor()

# cursor.execute('''

#     CREATE TABLE students2(
#         id INTEGER PRIMARY KEY,
#         name CHAR(20),
#         class_id INTEGER           
#     )

# ''')

# cursor.execute('''

#             CREATE TABLE class(
#                id INTEGER PRIMARY KEY,
#                subjext CHAR(20) 
#                )

#                ''')

# cursor.execute("INSERT INTO students2 (name, class_id) VALUES ('John', 101)")
# cursor.execute("INSERT INTO students2 (name, class_id) VALUES ('Alice', 102)")
# cursor.execute("INSERT INTO students2 (name, class_id) VALUES ('Bob', 101)")
# cursor.execute("INSERT INTO students2 (name, class_id) VALUES ('test', 112)")

# cursor.execute("INSERT INTO class (id, subjext) VALUES (101, 'Math')")
# cursor.execute("INSERT INTO class (id, subjext) VALUES (102, 'Science')")
# cursor.execute("INSERT INTO class (id, subjext) VALUES (103, 'Eng')")

# cursor.execute(
# """
# select students2.name, class.subjext 
# FROM students2
# INNER JOIN class ON students2.class_id = class.id
# """
# )

"""

cursor.execute(

SELECT students2.name, class.subjextts2
CROSS JOIN class;


)
"""

cursor.execute('''

    SELECT students2.name, class.subjext
    FROM students2
    INNER JOIN class ON students2.class_id = class.id 

''')
rows = cursor.fetchall()

# connection.commit()


for row in rows:
    print(row)


