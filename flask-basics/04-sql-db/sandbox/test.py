# pylint: disable=C0111,C0103
# - [C0111] is a warning when missing function docstrings.
# - [C0103] WARNING: constant names not UPPER_CASE style.
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# CREATE A TABLE
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# INSERT A SINGLE ROW
user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

# INSERT MULTIPLE ROWS
users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz'),
    (4, 'linh', 'password')
]
cursor.executemany(insert_query, users)

# SELECT ROWS
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
