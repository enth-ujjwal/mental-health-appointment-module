from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":

        # Retrieve form values
        name = request.form.get("name")
        email = request.form.get("email")
        date = request.form.get("date")
        time = request.form.get("time")

        # Retrieve credentials from .env
        sender_email = os.getenv("EMAIL_ID")
        sender_password = os.getenv("EMAIL_PASSWORD")

        # Compose email
        message = MIMEMultipart("alternative")
        message["Subject"] = "Mental Health Appointment Confirmation"
        message["From"] = sender_email
        message["To"] = email

        text = f"Hello {name}, your mental health appointment is booked on {date} at {time}."

        html = f"""
        <html>
          <body>
            <h2>Hello {name}</h2>
            <p>Your mental health appointment is booked on <b>{date}</b> at <b>{time}</b>.</p>
            <p>Thank you for trusting us.</p>
          </body>
        </html>
        """

        message.attach(MIMEText(text, "plain"))
        message.attach(MIMEText(html, "html"))

        # SMTP sending (secure)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())
            server.quit()
            print("Email sent successfully")
        except Exception as e:
            print("Error sending email:", e)

        return render_template("thankyou.html", user_name=name)

    return render_template("book.html")


if __name__ == "__main__":
    app.run(debug=True)
