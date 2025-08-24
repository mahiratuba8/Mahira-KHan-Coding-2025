# Connect with sqlite database
import sqlite3
import pandas as pd

conn = sqlite3.connect('database.sqlite')
print("Opened database successfully")

# Create table (only create if not exists, to avoid errors if rerun)
conn.execute('''CREATE TABLE IF NOT EXISTS CLASS_10
        (SNO INT PRIMARY KEY NOT NULL,
        Roll_No INT NOT NULL,
        Name TEXT NOT NULL,
        AGE INT DEFAULT (15),
        GENDER TEXT NOT NULL,
        Email_ID TEXT NOT NULL,
        Contact_No REAL NOT NULL);''')
print("Table created successfully")

# Insert data (use INSERT OR IGNORE to avoid duplicate key errors)
conn.execute("INSERT OR IGNORE INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
      VALUES (1, 1, 'Allen', 14, 'Male', 'allen@gmail.com', 8080900 )")

conn.execute("INSERT OR IGNORE INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
      VALUES (2, 2, 'Aisha', 14, 'Female', 'aish@gmail.com', 9080900 )")

conn.execute("INSERT OR IGNORE INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
      VALUES (3, 3, 'Jeff', 15, 'Male', 'jeff@gmail.com', 9900900 )")

conn.commit()
print("Records created successfully")

# Show all tables
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("\nTables in DB:\n", tables)

# Show CLASS_10 data
class_10d = pd.read_sql("SELECT * FROM CLASS_10;", conn)
print("\nCLASS_10 Table:\n", class_10d)
