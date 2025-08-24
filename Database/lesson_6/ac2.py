# Import necessary libraries
import pandas as pd
import sqlite3

# Connect with sqlite database
database = 'database.sqlite'
conn = sqlite3.connect(database)
print("Opened database successfully")

# Display all tables of the database
df = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("\nTables in DB:\n", df)

# ---- Only run next queries if the tables exist ----
if "Player_Match" in df['name'].values:
    # Display first 5 rows of Player_Match
    player_match = pd.read_sql("SELECT * FROM Player_Match;", conn)
    print("\nPlayer_Match (first 5 rows):\n", player_match.head())

    # Check null values in Team_Id column
    null_player_match = pd.read_sql("SELECT * FROM Player_Match WHERE Team_Id IS NULL;", conn)
    print("\nNull Player_Match rows:\n", null_player_match)
else:
    print("\n⚠️ 'Player_Match' table not found in DB.")

if "Match" in df['name'].values:
    # Display first 5 rows of Match
    toss_dec = pd.read_sql("SELECT * FROM Match;", conn)
    print("\nMatch (first 5 rows):\n", toss_dec.head())

    # Check null values in Match_Winner column
    null_match = pd.read_sql("SELECT * FROM Match WHERE Match_Winner IS NULL;", conn)
    print("\nNull Match rows:\n", null_match)
else:
    print("\n⚠️ 'Match' table not found in DB.")
