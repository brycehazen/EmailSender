@echo off
REM Setting Flask environment variables
set FLASK_APP=app.py
set FLASK_ENV=development

REM Start the Flask server in the background
start /b flask run

REM Pause to ensure the server starts before opening the browser
timeout /T 5

REM Open the default browser
start http://localhost:5000
