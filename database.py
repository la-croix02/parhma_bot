import sqlite3

conn = sqlite3.connect("survey.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS survey(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
q1 TEXT,
q2 TEXT,
q3 TEXT,
q4 TEXT
)
""")
conn.commit()

def save_survey(user_id, q1, q2, q3, q4):
    cursor.execute(
        "INSERT INTO survey(user_id,q1,q2,q3,q4) VALUES(?,?,?,?,?)",
        (user_id, q1, q2, q3, q4)
    )
    conn.commit()

def get_stats():
    stats = {}
    for q in ["q1", "q2", "q3", "q4"]:
        cursor.execute(f"SELECT {q}, COUNT(*) FROM survey GROUP BY {q}")
        stats[q] = cursor.fetchall()
    return stats

def get_total():
    cursor.execute("SELECT COUNT(*) FROM survey")
    return cursor.fetchone()[0]