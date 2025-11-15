import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def send_daily_log():
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receiver = os.getenv("EMAIL_TO")

    # Find the latest log file
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        return "No logs directory found."
    log_files = sorted(os.listdir(logs_dir))
    if not log_files:
        return "No log files found."
    latest_log = os.path.join(logs_dir, log_files[-1])

    with open(latest_log, "r", encoding="utf-8") as f:
        log_content = f.read()

    # Prepare email
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = f"AI Job Applier Summary – {datetime.now().strftime('%Y-%m-%d')}"

    body = f"""
    Hello Bhargav 👋,

    Here is today's AI Job Applier summary:

    {log_content[:4000]}

    ✅ Automated job application run completed.

    – Your AI Job Applier Bot 🤖
    """
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
        print("✅ Email summary sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
