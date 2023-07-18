---

# Flask Email Sender

A simple Flask application to send emails using SMTP, with an interface for uploading a CSV file of recipients and editing the email template.

## Files

1. `app.py` - The main Python script that runs the Flask server. It handles the routing for the application, including the upload of the CSV file, editing of the email template, previewing of the email, and the sending of the emails.

2. `start.bat` - A batch script to start the Flask server and open the application in a web browser (for Windows users).

3. `templates/index.html` - The initial webpage that users see. It contains a form for uploading the CSV file and a textarea for editing the email template.

4. `templates/preview.html` - The second webpage that users see after submitting the form on `index.html`. It previews the first email using the data from the first row of the CSV file and lists all the recipient email addresses.

## Setup Instructions

1. Install Python: You need to have Python installed on your machine. You can download it from the [official website](https://www.python.org/downloads/). 

2. Install Flask: Open a command prompt or terminal and install Flask using pip:

    ```
    pip install flask
    ```

3. Install pandas: Similarly, install pandas using pip:

    ```
    pip install pandas
    ```

4. Clone or download this repository to your local machine.

5. Update `app.py` with your SMTP server details (server, port, email, and password).

6. Open `start.bat` (Windows) to start the Flask server and open the application in your default web browser.

7. If you're on a different platform, you'll need to set the Flask environment variables and start the server manually. Here's how you can do it on a Unix-like system:

    ```
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run
    ```

    Then open a web browser and navigate to `http://localhost:5000`.

## Usage Instructions

1. On the initial webpage (`index.html`), select your CSV file and edit the email template as necessary. Click 'Next' to proceed.

2. On the second webpage (`preview.html`), review the first email and the list of recipient email addresses. If everything looks good, click 'Send Emails' to start sending the emails.

---

Please remember to modify the server details in `app.py` and to tailor the setup and usage instructions to fit your specific needs. This README provides a basic outline and may need to be expanded for a more comprehensive guide.
