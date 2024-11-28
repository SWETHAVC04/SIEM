import pandas as pd
from sklearn.ensemble import IsolationForest
import json

# Step 1: Load and process logs from the JSON file
def load_logs(input_file):
    with open(input_file, 'r') as file:
        logs = json.load(file)
    return pd.DataFrame(logs)

# Step 2: Preprocess logs (handle missing values and feature extraction)
def preprocess_logs(logs):
    # Extract relevant features (you can adjust these based on your log structure)
    features = logs[["status", "size"]]  # Adjust the columns as needed

    # Handle missing values (e.g., filling with mean or 0)
    features = features.fillna(0)  # Optionally replace NaNs with 0, or use features.mean() for other strategies

    return features

# Step 3: Detect anomalies using IsolationForest
def detect_anomalies(features):
    # Initialize the IsolationForest model with contamination rate (fraction of outliers)
    model = IsolationForest(contamination=0.1)

    # Fit the model and predict anomalies (1 for normal, -1 for anomaly)
    anomalies = model.fit_predict(features)

    return anomalies

# Step 4: Apply anomaly detection and flag suspicious logs
def apply_anomaly_detection(input_file, output_file):
    # Load and preprocess logs
    logs = load_logs(input_file)
    features = preprocess_logs(logs)

    # Detect anomalies
    anomalies = detect_anomalies(features)

    # Flag anomalies in the original logs
    logs['anomaly'] = anomalies

    # Filter and display anomalies (logs where anomaly == -1)
    anomalies_df = logs[logs['anomaly'].isin([-1, 1])]

    # Save flagged anomalies to a new file (optional)
    anomalies_df.to_csv(output_file, index=False)
    print(f"Detected anomalies saved to {output_file}")
    print(anomalies_df)

# Run the script
if __name__ == "__main__":
    input_file = "parsed_logs.json"  # Input file containing parsed logs
    output_file = "anomalies.csv"    # Output file for detected anomalies

    apply_anomaly_detection(input_file, output_file)