import sqlite3

# Create or connect to a database. 
# It will connect to the database if exists, else create new one
conn = sqlite3.connect('/Users/Shared/db/abcOrg.db')

# Create a cursor
cursor = conn.cursor()

# create a table
cursor.execute("""
    CREATE TABLE employees (
        first_name TEXT, 
        last_name TEXT
    )
""")

# Define list of employees
employees_list = [
    ('Krishna', 'Gurram'), 
    ('Ram', 'Gurram'), 
    ('Sailu', 'PTR')
]

# Insert new records to the database
cursor.executemany("INSERT INTO employees VALUES (?, ?)", employees_list)

# print all the records from employees table
cursor.execute("SELECT rowid, * FROM employees")
records = cursor.fetchall()

for row in records:
    print(row)

# commit changes to the database
conn.commit()

# close the connection
conn.close()

print("Program finished successfully!!!!!")
