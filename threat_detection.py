import sqlite3
import psycopg2
from datetime import timedelta, datetime

# Database configuration
db_file = 'D:\Swetha\Cyber Security\SIEM\logs.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

DB_CONFIG = {
    "dbname": "siem_db",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
}

def detect_failed_logins():
    try:
        cursor.execute("SELECT timestamp, source, status FROM logs WHERE status = 'FAILED_LOGIN'")
        logs = cursor.fetchall()

        failed_logins = {}
        alerts = []

        # Analyze logs
        for log in logs:
            timestamp, source, status = log
            if source not in failed_logins:
                failed_logins[source] = []
            failed_logins[source].append(timestamp)

            # Check for threshold
            if len(failed_logins[source]) >= 5:
                if (failed_logins[source][-1] - failed_logins[source][0]) <= timedelta(minutes=2):
                    alerts.append(f"ALERT: Multiple failed logins detected from {source} at {failed_logins[source][-1]}")

        for alert in alerts:
            print(alert)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    detect_failed_logins()