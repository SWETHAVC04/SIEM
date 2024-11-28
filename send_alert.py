import smtplib
from email.mime.text import MIMEText

def send_alert(recipient, subject, message):
    smtp_server = "smtp.example.com"
    sender = "alerts@siem.com"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls()
        server.login("your_email", "your_password")
        server.send_message(msg)

if __name__ == "__main__":
    send_alert("admin@example.com", "Critical SIEM Alert", "Multiple failed logins detected!")