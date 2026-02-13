import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("genes.db")

# SQL query
query = """
SELECT species, AVG(length) AS avg_length
FROM genes
GROUP BY species;
"""

# Execute query and load into DataFrame
df = pd.read_sql_query(query, conn)

print("Average Gene Length per Species:")
print(df)

# Save to CSV
df.to_csv("average_gene_length.csv", index=False)

print("\nCSV file saved as average_gene_length.csv")

conn.close()
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("genes.db")

# SQL query
query = """
SELECT species, AVG(length) AS avg_length
FROM genes
GROUP BY species;
"""

# Execute query
df = pd.read_sql_query(query, conn)

print("Average Gene Length per Species:")
print(df)

conn.close()
