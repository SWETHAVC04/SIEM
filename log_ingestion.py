import re
import json
from datetime import datetime

# Parse raw log lines
def parse_log(log_line):
    # Updated regular expression to match the log structure
    pattern = re.compile(
        r'(?P<source>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>[\d-]+) "([^"]*)" "(?P<user_agent>[^"]*)"'
    )
    match = pattern.match(log_line)
    if match:
        fields = match.groupdict()
        # Convert the timestamp to a standard datetime format
        timestamp = datetime.strptime(fields["timestamp"], "%d/%b/%Y:%H:%M:%S %z")
        return {
            "timestamp": timestamp.isoformat(),  # Convert to ISO 8601 format for JSON compatibility
            "source": fields["source"],
            "request": fields["request"],
            "status": int(fields["status"]),
            "size": fields["size"] if fields["size"] != "-" else None,  # Handle cases where size is "-"
            "user_agent": fields["user_agent"],
        }
    else:
        raise ValueError(f"Log line does not match expected format: {log_line}")

# Read and parse logs
def process_logs(input_file, output_file):
    with open(input_file, "r") as log_file:
        logs = []
        for line in log_file:
            try:
                logs.append(parse_log(line.strip()))
            except ValueError as e:
                print(e)  # Log the error for invalid lines and continue processing
        with open(output_file, "w") as out_file:
            json.dump(logs, out_file, indent=2)
    print(f"Logs saved to {output_file}")

if __name__ == "__main__":
    process_logs("raw_logs.txt", "parsed_logs.json")