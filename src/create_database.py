import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv(
    'data/cleaned/hackernews_cleaned.csv'
)

# Create SQLite database
conn = sqlite3.connect(
    'hackernews.db'
)

# Export table
df.to_sql(
    'hackernews_posts',
    conn,
    if_exists='replace',
    index=False
)

print("Database created successfully.")

conn.close()
