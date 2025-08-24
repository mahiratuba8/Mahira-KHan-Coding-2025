import sqlite3


conn = sqlite3.connect("your_database.db")
cursor = conn.cursor()

print("Tables in database:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for row in cursor.fetchall():
    print(row[0])

print("\nTeam table columns:")
cursor.execute("PRAGMA table_info(Team);")
for row in cursor.fetchall():
    print(row)



print("\nTeams from Texas and New York:")
cursor.execute("""
    SELECT *
    FROM Team
    WHERE state IN ('Texas', 'New York');
""")
for row in cursor.fetchall():
    print(row)
