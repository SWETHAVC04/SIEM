import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import psycopg2
import sqlite3

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

def fetch_logs():
    cursor.execute("SELECT timestamp, size, source, status FROM logs")
    rows = cursor.fetchall()
    conn.close()

    # Convert to DataFrame
    return pd.DataFrame(rows, columns=["timestamp", "size", "source", "status"])

app = dash.Dash(__name__)
df = fetch_logs()

# Create a bar chart for log events
fig = px.histogram(df, x="timestamp", color="size", title="Log Event Trends")

app.layout = html.Div([
    html.H1("SIEM Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)