

import sqlite3
import os

# Step 2: Create a connection to a SQLite database and a cursor object
conn = sqlite3.connect('file_names.db')
c = conn.cursor()

# Step 3: Create a table with an auto-increment primary integer field and a string field
c.execute('''CREATE TABLE IF NOT EXISTS files
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL)''')

# Step 4: Read in the list of file names and filter out only the ones with a .txt extension
file_names = ['file1.txt', 'file2.png', 'file3.txt', 'file4.doc']
text_files = [file for file in file_names if file.endswith('.txt')]

# Step 5: Iterate through the filtered file names and insert them into the database table
for file in text_files:
    c.execute("INSERT INTO files (name) VALUES (?)", (file,))
    conn.commit()

# Step 6: Query the database table for all records and print out the qualifying text files to the console
c.execute("SELECT name FROM files")
rows = c.fetchall()
print("Qualifying text files:")
for row in rows:
    print(row[0])

# Close the connection to the database
conn.close()
