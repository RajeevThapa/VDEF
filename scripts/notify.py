import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_notification():
    # Path to the summary report
    report_path = "/home/rajeev/User_rajeev/AAU/AVDEF/scans/reports/summary_report.md"

    # Check if the report exists
    if not os.path.exists(report_path):
        print(f"Error: Report file '{report_path}' not found.")
        return

    # Read the report content
    with open(report_path, "r") as report_file:
        report_content = report_file.read()

    # Compose email
    msg = MIMEMultipart()
    msg['Subject'] = 'Automated Vulnerability Scan Report'
    msg['From'] = 'scanner@example.com'
    msg['To'] = 'team@example.com'

    # Email Body (Plain Text)
    msg.attach(MIMEText(report_content, 'plain'))

    # SMTP configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587  # Use 465 for SSL, 587 for TLS
    smtp_user = os.getenv('SMTP_USER', 'scanner@example.com')  # Use environment variable for username
    smtp_password = os.getenv('SMTP_PASSWORD', 'password')  # Use environment variable for password

    try:
        # Connect to SMTP server with TLS
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(smtp_user, smtp_password)
            server.send_message(msg)

        print("Notification sent successfully.")

    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_notification()
