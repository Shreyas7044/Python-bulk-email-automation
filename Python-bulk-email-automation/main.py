import smtplib
import csv
import os
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    return Template(template_content)


def main():
    # Load email template
    message_template = read_template('template.txt')

    # Email credentials
    MY_ADDRESS = input("Enter your Gmail address: ")
    PASSWORD = input("Enter your App Password: ")

    # Set up Gmail SMTP Server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(MY_ADDRESS, PASSWORD)

    # Read CSV File
    with open("details.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)   # Skip header row

        for row in reader:
            name = row[0]
            receiver_email = row[1]

            msg = MIMEMultipart()

            # Replace placeholders in template
            message = message_template.substitute(
                PERSON_NAME=row[0],
                MATH=row[2],
                ENG=row[3],
                SCI=row[4]
            )

            print("Sending to:", receiver_email)

            msg['From'] = MY_ADDRESS
            msg['To'] = receiver_email
            msg['Subject'] = "Mid Term Grades"

            msg.attach(MIMEText(message, 'plain'))

            server.send_message(msg)
            del msg

    server.quit()
    print("All Emails Sent Successfully!")


if __name__ == "__main__":
    main()