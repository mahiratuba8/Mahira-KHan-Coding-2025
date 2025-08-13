import sqlite3

import pandas as pd 

database= 'database.sqlite'
conn= sqlite3.connect(database)

print('analysing the tables')
print(f"connected to: {database}")

tables_df= pd.read_sql_query(""" SELECT NAME FROM sqlite_master WHERE type='table' """,conn)

print(f"\n table found in the database: {len(tables_df)}")

for table in tables_df['name']:
    print(f"{table}")

if 'matches' in tables_df['name'].values:
    matches= pd.read_sql_query("SELECT * FROM matches", conn)
    print(f"columns: {list(matches.columns)}")
    print("\n table info")
    matches.info()
    print("\n First five rows on the match table: ")
    print(matches.head())
    print("\n Colomn analysis")
    for col in matches.columns:
        print(f"{col}:{matches[col].dtype}")
else:
    print("\n matches table not found, available table: ")
    for table in tables_df['name']:
        print(f"\n table: {table}")
        df=pd.read_sql_query(f"SELECT * FROM {table}", conn)
        print(f"rows: {len(df)}, columns:{len(df.columns)}")
        print(f"columns:{list(df.columns)}")
        print("sample data")
        print(df.head(3))
conn.close()
print("\n analysis complete")