
import pandas as pd
import sqlite3
database = 'database.sqlite'

connection = sqlite3.connect("your_database.db")
print("Opened database successfully.")


query = "SELECT name FROM sqlite_master WHERE type='table';"
tables_df = pd.read_sql_query(query, connection)

print("Tables and database")
print(query)


