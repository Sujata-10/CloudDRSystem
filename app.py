from flask i else:
        return "<h1>Invalid Username or Password</h1>"
nano app.py
# Upload Route
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':

        file = request.files['file']

        if file:

            filename = secure_filename(file.filename)

            file.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    filename
                )
            )

            return "<h1>File Uploaded Successfully</h1>"

    return render_template('upload.html') 
# Run Flask
if __name__ == '__main__':

 nano app.py    app.run(host='0.0.0.0', port=5000)
nano app.pymport Flask, render_template, request
import pymysql
import psutil
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Upload Folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Database Connection
db = pymysql.connect(
    host="localhost",
    user="flaskuser",
    password="password123",
    database="cloud_dr_system"
)
#Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Login Route
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor()

    query = "SELECT * FROM users WHERE username=%s AND password>

    cursor.execute(query, (username, password))

    result = cursor.fetchone()

    if result:

        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent

        return render_template(
            'dashboard.html',
            cpu=cpu,
            memory=memory
        )
else:
        return "<h1>Invalid Username or Password</h1>"
nano app.py
# Upload Route
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':

        file = request.files['file']

        if file:

            filename = secure_filename(file.filename)

            file.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    filename
                )
            )

            return "<h1>File Uploaded Successfully</h1>"

    return render_template('upload.html')

# Run Flask
if __name__ == '__main__':

 nano app.py    app.run(host='0.0.0.0', port=5000)
nano app.py