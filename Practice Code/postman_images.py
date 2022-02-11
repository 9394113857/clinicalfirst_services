# image.py
from flask import Flask, render_template, redirect, request, flash
from flask_mysqldb import MySQL, MySQLdb  # pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
from werkzeug.utils import secure_filename
import os
# import magic
import urllib.request
from datetime import datetime

app = Flask(__name__)

app.secret_key = "caircocoders-ednalan"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'raghu'
app.config['MYSQL_DB'] = 'clinicalfirst_services'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

UPLOAD_FOLDER = 'C:/Users/Raghu/Downloads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
path = 'C:/Users/Raghu/Downloads'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'pdf', 'csv', 'xlsx'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/IMG_UPLOAD", methods=["POST"])
def upload():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    now = datetime.now()
    if request.method == 'POST':

        # files = request.files.getlist('files[]')
        files = request.files('files')
        # print(files)
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                cursor.execute("INSERT INTO images (file_name, uploaded_on) VALUES (%s, %s)", [filename, now])
                mysql.connection.commit()
            print(file)
        cur.close()
        return "Files Uploaded Successfully !!!"


if __name__ == "__main__":
    app.run(debug=True)
