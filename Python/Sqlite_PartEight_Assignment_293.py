

c.execute("SELECT FirtName, LastName FROM People WHERE Age > 30")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)
