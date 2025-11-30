#  Mental Health Appointment Booking Module (Flask)

A standalone backend module for booking mental health appointments using Flask.  
This project allows users to schedule an appointment by entering their details and automatically sends them a confirmation email using Gmail SMTP.

This module is a part of a larger team project but is fully functional independently.  
It demonstrates backend concepts like routing, form handling, email sending, environment variables, and clean project structure.


##  Features

-  Appointment booking (Name, Email, Date, Time)
- Automatic confirmation email via Gmail SMTP
-  Secure handling of email credentials (no passwords stored in code)
-  Modular Flask routes
-  HTML templates rendered with Jinja2
-  Ready to integrate into larger Flask or React applications

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **Jinja2**
- **SMTP (Gmail App Password)**
- **HTML (basic templating)**

---

## 📁 Folder Structure
mental_health_app/
│── app.py
│── resources.json (optional for future expansion)
│── templates/
│ ├── index.html
│ ├── book.html
│ └── thankyou.html
│── static/ (optional)
│── README.md


---

▶️ How to Run

Install requirements

pip install flask python-dotenv


Create .env file

EMAIL_ID=your_gmail
EMAIL_PASSWORD=your_app_password


Run the server

python app.py

Open:

http://127.0.0.1:5000/

🔐 Security

This project uses .env file for sensitive data.
Do not store passwords inside your Python code.


Ujjwal Singh
Backend Developer | Python | Flask

