from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/upload', methods=['POST'])
def upload_file():

    file = request.files['file']

    if file:

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            file.filename
        )

        file.save(filepath)

        file_size = round(
            os.path.getsize(filepath) / 1024,
            2
        )

        upload_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        file_extension = os.path.splitext(
            file.filename
        )[1]

        return render_template(
            'dashboard.html',
            filename=file.filename,
            filesize=file_size,
            uploadtime=upload_time,
            filetype=file_extension
        )

    return "No File Uploaded"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)