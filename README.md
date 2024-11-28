This repository contains a Python-based solution for detecting anomalous behavior in server log data. The primary goal is to identify outliers or abnormal patterns based on certain log attributes such as timestamps, source IPs, status codes, user agents, and response sizes. The solution uses Isolation Forest from Scikit-learn for unsupervised anomaly detection and visualizes the results with Matplotlib and Seaborn.

# Features
- Log Parsing: Reads and extracts fields from server log files.
- Data Preprocessing: Normalizes and processes the data for anomaly detection.
- Anomaly Detection: Identifies anomalous logs using the Isolation Forest algorithm.
- Visualization: Highlights anomalies in a scatter plot, making it easy to visualize outliers in the data.
- Customizable: User can configure the log file path and customize the anomaly detection parameters.

# Usage
## For Anomaly table
'''
python flask_display.py
'''

## For visualization
'''
python siem_dashboard.py
'''
