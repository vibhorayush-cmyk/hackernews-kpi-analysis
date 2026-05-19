import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect(
    'hackernews.db'
)

# SQL query
query = """
SELECT
    title,
    points
FROM hackernews_posts
ORDER BY points DESC
LIMIT 10;
"""

# Execute query
result = pd.read_sql_query(
    query,
    conn
)

# Print result
print("\nTop Performing Posts:\n")

print(result)

# Close connection
conn.close()
