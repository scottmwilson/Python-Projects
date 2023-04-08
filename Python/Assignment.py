Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> import sqlite3
>>> connection  sqlite3.connect("C:\Users\scott\OneDrive\Documents\Python-Projects\Python\test_database.db")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> connection  sqlite3.connect("C:\Users\scott\OneDrive\Documents\Python-Projects\Python test_database.db")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> connection  sqlite3.connect("C:/Users/scott/OneDrive/Documents/Python-Projects/Python/test_database.db")
SyntaxError: invalid syntax
>>> connection = sqlite3.connect("C:/Users/scott/OneDrive/Documents/Python-Projects/Python/test_database.db")
>>> 
>>> c = connection.cursor()
>>> c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
<sqlite3.Cursor object at 0x0000029EFE44A5C0>
>>> c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
<sqlite3.Cursor object at 0x0000029EFE44A5C0>
>>> connection.commit()
>>> connection = sqlite2.connect(':memory:')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    connection = sqlite2.connect(':memory:')
NameError: name 'sqlite2' is not defined. Did you mean: 'sqlite3'?
>>> connection = sqlite3.connect(':memory:')
>>> c.execute("DROP TABLE if EXISTS People")
<sqlite3.Cursor object at 0x0000029EFE44A5C0>
>>> connection.close()
>>> 
>>> with sqlite3.connect("test_database.db") as connection:
...     # perform any SQL operations using connection here
... 
... import sqlite3
SyntaxError: expected an indented block after 'with' statement on line 1
>>> with
SyntaxError: incomplete input
>>> with sqlite2.connect('test_database.db') as connection
SyntaxError: incomplete input
>>> with sqlite3.connect('test_database.db') as connection:
...     c = connection.cursor()
...     c.executescript("""DROP TEABLE IF EXISTS People; CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT); INSERT INTO People VALUES('Ron', 'Obvious', '42'); """)
... 
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    with sqlite3.connect('test_database.db') as connection:
sqlite3.OperationalError: unable to open database file
>>> 
>>> peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
>>> 
>>> c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
sqlite3.OperationalError: no such table: People
>>> c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
sqlite3.OperationalError: no such table: People
>>> 
================================================================== RESTART: C:/Users/scott/OneDrive/Documents/Python-Projects/Python/Sqlite_PartFive_Assignment_290.py =================================================================
Enter your first name: Scott
Enter your last name: Wilson
Enter your age: 38
Traceback (most recent call last):
  File "C:/Users/scott/OneDrive/Documents/Python-Projects/Python/Sqlite_PartFive_Assignment_290.py", line 13, in <module>
    c.execute(line)
sqlite3.OperationalError: no such table: People

================================================================== RESTART: C:/Users/scott/OneDrive/Documents/Python-Projects/Python/Sqlite_PartSix_Assignment_291.py ==================================================================
Enter your first name: Scott
Enter your last name: Wilson
Enter your age: 38
Traceback (most recent call last):
  File "C:/Users/scott/OneDrive/Documents/Python-Projects/Python/Sqlite_PartSix_Assignment_291.py", line 14, in <module>
    c.execute(line, personData)
sqlite3.OperationalError: no such table: People
