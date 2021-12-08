import sqlite3

# Create or connect to a database. 
# It will connect to the database if exists, else create new one
conn = sqlite3.connect('/Users/Shared/db/abcOrg.db')

# Create a cursor
cursor = conn.cursor()

# create a table
cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        first_name TEXT, 
        last_name TEXT
    )
""")

# Insert new records to the database
cursor.execute("INSERT INTO employees VALUES (1, 'Krishna', 'Gurram')")
cursor.execute("INSERT INTO employees VALUES (2, 'Ram', 'Gurram')")

# commit changes to the database
conn.commit()

# close the connection
conn.close()

print("Program finished successfully!!!!!")