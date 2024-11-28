import sqlite3
import json

def load_logs_to_db(input_file, db_file):
    # Connect to SQLite (or create the database file if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            source TEXT,
            request TEXT,
            status INTEGER,
            size INTEGER,
            user_agent TEXT
        )
    """)

    # Load logs from JSON file
    with open(input_file, "r") as file:
        logs = json.load(file)
        for log in logs:
            cursor.execute("""
                INSERT INTO logs (timestamp, source, request, status, size, user_agent)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                log["timestamp"], log["source"], log["request"], 
                log["status"], log["size"], log["user_agent"]
            ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Logs loaded into {db_file}")

if __name__ == "__main__":
    load_logs_to_db("parsed_logs.json", "logs.db")