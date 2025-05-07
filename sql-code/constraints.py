import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# cursor.execute('''

#     CREATE TABLE department(
#     id INTEGER PRIMARY KEY,
#     name CHAR(100)
#     )

# ''')

# cursor.execute('''

#     CREATE TABLE employee(
#     id INTEGER PRIMARY KEY,
#     name CHAR(100),   
#     dep_id INTEGER,
#     FOREIGN KEY(dep_id) REFERENCES department(id)    
#             ON DELETE CASCADE    
#     )

# ''')

# cursor.execute('INSERT INTO department (name) VALUES ("HR")')
# cursor.execute('INSERT INTO department (name) VALUES ("Finance")')


# cursor.execute('INSERT INTO employee (name, dep_id) VALUES ("harsh", 1)')
# cursor.execute('INSERT INTO employee (name, dep_id) VALUES ("kishan", 2)')

# cursor.execute('DROP TABLE department')
# cursor.execute('DROP TABLE employee')

cursor.execute('DELETE FROM department WHERE id=2')

conn.commit()