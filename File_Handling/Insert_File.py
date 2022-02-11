import MySQLdb
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "Raghu"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'raghu'
app.config['MYSQL_DB'] = 'clinicalfirst_services'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


thedata = open('D:\\Project\\clinicalfirst_services\\Raghu\\results.txt', 'rb').read()
sql = "INSERT INTO images (file_name) VALUES (%s)"
# cursor initialized:-
cursor = mysql.connection.cursor()
# cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute(sql, (thedata))
mysql.connection.commit()
print("Data Inserted")
cursor.close()

if __name__ == "__main__":
    app.run(debug=True)


# now = datetime.now()

# query = "INSERT INTO images VALUES (%s, %s)"
# query = "INSERT INTO images (file_name, uploaded_on) VALUES (%s, %s)", [file_content, now]

# import mysql.connector
#
# def convertToBinaryData(filename):
#     # Convert digital data to binary format
#     with open(filename, 'rb') as file:
#         binaryData = file.read()
#     return binaryData
#
#
# def insertBLOB(emp_id, name, photo, biodataFile):
#     print("Inserting BLOB into python_employee table")
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='clinicalfirst_services',
#                                              user='root',
#                                              password='raghu')
#
#         cursor = connection.cursor()
#         sql_insert_blob_query = """ INSERT INTO python_employee
#                           (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""
#
#         empPicture = convertToBinaryData(photo)
#         file = convertToBinaryData(biodataFile)
#
#         # Convert data into tuple format
#         insert_blob_tuple = (emp_id, name, empPicture, file)
#         result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
#         connection.commit()
#         print("Image and file inserted successfully as a BLOB into python_employee table", result)
#
#     except mysql.connector.Error as error:
#         print("Failed inserting BLOB data into MySQL table {}".format(error))
#
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")
#
# insertBLOB(1, "Eric", "D:\Project\clinicalfirst_services\Raghu\spider-man.png",
#            "D:\Project\clinicalfirst_services\Raghu\results.txt")

# insertBLOB(2, "Scott", "D:\Project\clinicalfirst_services\Raghu\scott_photo.png",
#            "D:\Project\clinicalfirst_services\Raghu\scott_bioData.txt")