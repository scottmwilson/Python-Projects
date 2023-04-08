import sqlite3

# Step 1: Create a database table in RAM named Roster
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE Roster (Name TEXT, Species TEXT, IQ INT)''')

# Step 2: Populate the table with values
c.execute("INSERT INTO Roster VALUES ('Jean-Baptiste Zorg', 'Human', 122)")
c.execute("INSERT INTO Roster VALUES ('Korben Dallas', 'Meat Popsicle', 100)")
c.execute("INSERT INTO Roster VALUES ('Ak\\\'not', 'Mangalore', -5)")

# Step 3: Update Korben Dallas's species to be Human
c.execute("UPDATE Roster SET Species='Human' WHERE Name='Korben Dallas'")

# Step 4: Display names and IQs of all Humans in the table
c.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
for row in c.fetchall():
    print(row[0] + ' has an IQ of ' + str(row[1]))
