import sqlite3

conn = sqlite3.connect("token_usage.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS token_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
    prompt_tokens INTEGER,
    completion_tokens INTEGER,
    model TEXT,
    vendor TEXT
)
""")

cursor.execute("""
INSERT INTO token_usage (prompt_tokens, completion_tokens, model, vendor)
VALUES (?, ?, ?, ?)
""", (42, 58, "gpt-4o", "OpenAI"))

conn.commit()

cursor.execute("SELECT * FROM token_usage")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()