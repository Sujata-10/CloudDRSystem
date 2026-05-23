from flask import Flask, render_template, request, redirect, session
import os
import shutil
import psutil
from datetime import datetime

app = Flask(__name__)

app.secret_key = "secretkey"

UPLOAD_FOLDER = 'uploads'
BACKUP_FOLDER = 'backups'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(BACKUP_FOLDER, exist_ok=True)


# HOME PAGE
@app.route('/')
def home():

    if 'user' in session:
        return redirect('/dashboard')

    return redirect('/login')


# LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin123':

            session['user'] = username

            return redirect('/dashboard')

        else:
            return "Invalid Username or Password"

    return render_template('login.html')


# DASHBOARD
@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect('/login')

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    files = os.listdir(UPLOAD_FOLDER)

    return render_template(
        'dashboard.html',
        cpu=cpu,
        memory=memory,
        files=files
    )


# FILE UPLOAD
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':

        file = request.files['file']

        if file.filename != '':

            file.save(
                os.path.join(
                    UPLOAD_FOLDER,
                    file.filename
                )
            )

            return "File Uploaded Successfully"

    return render_template('upload.html')


# CREATE BACKUP
@app.route('/backup')
def backup():

    if 'user' not in session:
        return redirect('/login')

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_path = os.path.join(
        BACKUP_FOLDER,
        f'backup_{timestamp}'
    )

    shutil.copytree(
        UPLOAD_FOLDER,
        backup_path
    )

    return "Backup Created Successfully"


# RESTORE BACKUP
@app.route('/restore')
def restore():

    if 'user' not in session:
        return redirect('/login')

    backups = sorted(os.listdir(BACKUP_FOLDER))

    if not backups:
        return "No Backup Found"

    latest_backup = os.path.join(
        BACKUP_FOLDER,
        backups[-1]
    )

    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)

    shutil.copytree(
        latest_backup,
        UPLOAD_FOLDER
    )

    return "System Restored Successfully"


# LOGOUT
@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)