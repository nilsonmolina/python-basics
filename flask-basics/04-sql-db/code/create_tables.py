# pylint: disable=C0111,C0103
# - [C0111] is a warning when missing function docstrings.
# - [C0103] WARNING: constant names not UPPER_CASE style.
import sqlite3

# -------- OPEN DB CONNECTION --------
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# -------- CREATE USERS TABLE --------
create_table = ("CREATE TABLE IF NOT EXISTS users "
                "(id INTEGER PRIMARY KEY, username text, password text)")
cursor.execute(create_table)

# users = [
#     (2, 'rolf', 'asdf'),
#     (3, 'anne', 'xyz'),
#     (4, 'linh', 'password')
# ]
# cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", users)

# -------- CREATE ITEMS TABLE --------
create_table = ("CREATE TABLE IF NOT EXISTS items "
                "(name text, price real)")
cursor.execute(create_table)

# cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

# -------- COMMIT & CLOSE DB --------
connection.commit()
connection.close()
