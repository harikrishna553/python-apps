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
        last_name TEXT, 
        city TEXT
    )
""")

# Define list of employees
employees_list = [
    (1, 'Krishna', 'Gurram', 'Chennai'), 
    (2, 'Ram', 'Gurram', 'Bangalore'), 
    (3, 'Sailu', 'PTR', 'Chennai')
]

# Insert new records to the database
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees_list)
cursor.execute("SELECT rowid, * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("""
    UPDATE employees SET city = 'Hyderabad' 
        WHERE id = 1
""")

print('\nupdated the city to Hyderabad of employee 1\n')

cursor.execute("SELECT rowid, * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)


# commit changes to the database
conn.commit()

# close the connection
conn.close()

print("Program finished successfully!!!!!")