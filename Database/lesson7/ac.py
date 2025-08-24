# Import Necessary Libraries
import numpy as np
import pandas as pd
import sqlite3

# Setup connection with database
# Make sure the file 'database.sqlite' is in the same folder as this script
database = 'database.sqlite'
conn = sqlite3.connect(database)

# Display all tables in the database
tables = pd.read_sql("""
    SELECT name 
    FROM sqlite_master 
    WHERE type='table';
""", conn)

print("Tables in database:")
print(tables)

# Check how Inner Join works
joined_city = pd.read_sql("""
    SELECT c.Country_Id, c.Country_Name, ci.City_Name
    FROM country c
    INNER JOIN city ci
    ON c.Country_Id = ci.Country_id
""", conn)

print("\nInner Join Result:")
print(joined_city.head())

# Check how Outer Join (LEFT JOIN) works
joined_left = pd.read_sql("""
    SELECT *
    FROM player
    LEFT JOIN season
    ON player.Player_Id = season.Man_of_the_Series
""", conn)

print("\nLeft Join Result:")
print(joined_left.head())

# Check how Cross Join works
joined_cross = pd.read_sql("""
    SELECT c.Country_Id, c.Country_Name, ci.City_Name
    FROM country c
    CROSS JOIN city ci
""", conn)

print("\nCross Join Result:")
print(joined_cross.head())

# Check how Union Clause works
union = pd.read_sql("""
    SELECT Player_Name 
    FROM player
    UNION
    SELECT Team_Name 
    FROM team
""", conn)

print("\nUnion Result:")
print(union.head())

# Close connection
conn.close()
