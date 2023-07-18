from flask import Flask, render_template, request, redirect, url_for
import csv
import smtplib

app = Flask(__name__)

# Home route - displays the form
@app.route('/')
def home():
    return render_template('index.html')

# Send emails route - handles the form submission and sends the emails
@app.route('/send_emails', methods=['POST'])
def send_emails():
    # Get form data
    csv_file = request.files['csv_file']
    email = request.form['email']
    password = request.form['password']
    email_body = request.form['email_body']

    # Read the CSV file
    csv_data = csv_file.read().decode('utf-8').splitlines()
    csv_reader = csv.reader(csv_data)
    next(csv_reader)  # Skip the header row

    # Send emails
    for row in csv_reader:
        email_address = row[0]
        subject = row[1]
        body = row[2]

        # Send the email using smtplib
        message = f"Subject: {subject}\n\n{email_body}"
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email_address, message)

    return 'Emails sent successfully!'

if __name__ == '__main__':
    app.run()
