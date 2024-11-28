from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Function to read the anomalies data
def load_anomalies_data():
    # Load the CSV containing the anomaly results (generated earlier)
    df = pd.read_csv('anomalies.csv')
    return df

# Route to display the anomalies in a table
@app.route('/')
def index():
    anomalies_data = load_anomalies_data()
    return render_template('index.html', data=anomalies_data)

if __name__ == "__main__":
    app.run(debug=True)