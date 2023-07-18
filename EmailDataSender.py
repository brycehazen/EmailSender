from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

app = Flask(__name__)
app.secret_key = 'your secret key'  # for flash messaging

# Define your email credentials
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
email_user = 'youremail@outlook.com'
email_pass = 'yourpassword'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    if 'csvfile' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['csvfile']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    df = pd.read_csv(file)
    email_template = request.form['email_template']
    preview_email = email_template.format(name=df.loc[0, 'name'], donation_amount=df.loc[0, 'donation_amount'])
    return render_template('preview.html', preview_email=preview_email, emails=df['email'].tolist())

@app.route('/send', methods=['POST'])
def send():
    file = request.files['csvfile']
    df = pd.read_csv(file)
    email_template = request.form['email_template']
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.login(email_user, email_pass)
    for index, row in df.iterrows():
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = row['email']
        msg['Subject'] = 'Fundraiser update'
        body = email_template.format(name=row['name'], donation_amount=row['donation_amount'])
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(email_user, row['email'], text)
    server.quit()
    flash('Emails sent successfully.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
