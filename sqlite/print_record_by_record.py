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

# Define list of employees
employees_list = [
    (1, 'Krishna', 'Gurram'), 
    (2, 'Ram', 'Gurram'), 
    (3, 'Sailu', 'PTR')
]

# Insert new records to the database
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?)", employees_list)

# print all the records from employees table
cursor.execute("SELECT * FROM employees")
records = cursor.fetchall()
names = [description[0] for description in cursor.description]

for row in records:
    print(names[0], ':', row[0], ', ',names[1], ':', row[1], ', ', names[2], ':', row[2])

# commit changes to the database
conn.commit()

# close the connection
conn.close()

print("Program finished successfully!!!!!")
