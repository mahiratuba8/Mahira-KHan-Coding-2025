# Import necessary libraries
import sqlite3
import pandas as pd
import os

# --------------------------
# 1. Connect with SQLite Database
# --------------------------

# Change this path to where your database.sqlite file is stored
database = os.path.join(os.getcwd(), "database_1.sqlite")

# Connect to SQLite database
conn = sqlite3.connect(database)
print("Opened database successfully")

# --------------------------
# 2. View all tables in the database
# --------------------------
tables = pd.read_sql("""
    SELECT * 
    FROM sqlite_master
    WHERE type='table';
""", conn)
print(tables)

# --------------------------
# 3. Read 'Match' table into DataFrame
# --------------------------
matches = pd.read_sql("""
    SELECT *
    FROM Match;
""", conn)
print(matches.head())

# --------------------------
# 4. Queries
# --------------------------

# Get the Average Win Margin of all winning teams for Season 9
print("\nGet the Average Win Margin of all winning teams for Season 9")
result1 = pd.read_sql("""
    SELECT AVG(Win_Margin), Match_Winner
    FROM Match
    WHERE Season_Id = 9
    GROUP BY Match_Winner
    ORDER BY AVG(Win_Margin);
""", conn)
print(result1)

# Get the count of distinct venues for Season 9
print("\n Get the count of distinct venues for Season 9")
result2 = pd.read_sql("""
    SELECT COUNT(DISTINCT Venue_Id) AS VenueCount
    FROM Match
    WHERE Season_Id = 9;
""", conn)
print(result2)

# Get Min, Max, Avg Win Margin + Count of distinct Man_of_the_Match
print("\n Get Min, Max, Avg Win Margin + Count of distinct Man_of_the_Match")
result3 = pd.read_sql("""
    SELECT MIN(Win_Margin) AS MinMargin,
           MAX(Win_Margin) AS MaxMargin,
           AVG(Win_Margin) AS AvgMargin,
           COUNT(DISTINCT Man_of_the_Match) AS UniqueMoM
    FROM Match;
""", conn)
print(result3)

# Return total win_margins for all winners in Season 9
print("\n Return total win_margins for all winners in Season 9")
result4 = pd.read_sql("""
    SELECT SUM(Win_Margin) AS TotalMargin
    FROM Match
    WHERE Season_Id = 9;
""", conn)
print(result4)

# Close the connection
print("\n Closing the connectioh")
conn.close()
