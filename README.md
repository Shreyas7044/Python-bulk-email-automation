# Python-bulk-email-automation
This project demonstrates how to send personalized bulk emails using Python. It automates sending exam result emails to multiple recipients using a template and CSV data. Useful for teachers, teams, and anyone needing customized automated email delivery.

# Send Emails with Python – Bulk Personalized Email Automation

Sometimes we need to send emails to multiple people in a personalized way. Although the email format remains the same, the information changes for each recipient. This project shows how to automatically send personalized emails using Python.

Sending emails manually takes time and increases chances of human error. Python helps automate this entire process efficiently.

---

## 📌 Features
- Send emails to multiple people automatically
- Uses email template
- Reads user details from CSV
- Custom message per recipient
- Secure login
- Works with Gmail SMTP

---

## 🧠 How It Works

1️⃣ Create `template.txt` that contains the email body format  
Example:

Dear ${PERSON_NAME},
You have secured the following marks in your mid-term exams:
Math - ${MATH}
English - ${ENG}
Science - ${SCI}

2️⃣ Create `details.csv` containing recipient data  
Example:

NAME,EMAIL,MATH,ENG,SCI  
John,john@gmail.com,90,85,80  
Emma,emma@gmail.com,88,92,84  

3️⃣ Python reads CSV and fills template values  
4️⃣ Python sends customized emails automatically

---

## ⚙️ Requirements
Install Python 3.x

Then install required modules:
pip install -r requirements.txt


---

## 🔐 Gmail Security Note
Gmail no longer supports "Less Secure Apps".  
Enable:
- 2 Step Verification
- Create App Password
Use that password while running script.

---

## ▶️ How to Run the Project

1️⃣ Download/Clone Repository  
2️⃣ Ensure files exist:
- main.py
- template.txt
- details.csv

3️⃣ Run Script
python main.py


4️⃣ Enter Gmail & App Password  
5️⃣ Emails will be sent 🚀

---

## 🖼️ Screenshot
![Application Screenshot](screenshot.png)

---

## 🔁 Reusability
You can reuse this project for:
- Schools / Colleges
- Event Invitations
- Company Announcements
- Result Emails
- Personalized Campaign Emails

Just change CSV and Template file.

---

## 🤝 Contribution
Feel free to:
- Improve Code
- Add HTML email support
- Add Attachment Feature
Pull Requests Welcome!

---

## ❤️ Support
If you like the project, star ⭐ the repo.
