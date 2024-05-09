from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Function to get database connection
def get_db_connection():
    return pymysql.connect(
        host="0.0.0.0",
        user="root",
        password="NO",
        database="Airborne",
        cursorclass=pymysql.cursors.DictCursor
    )

# Function to close database connection
def close_db_connection(conn):
    conn.close()

@app.route('/home', methods=['GET'])
def get_home():
    return render_template('home.html')


@app.route('/login', methods=['POST'])
def login():
    passportNumber = request.form.get('pn')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Passenger where passportNumber = %s", (passportNumber,))
    users = cursor.fetchall()
    close_db_connection(conn)
    if not users:
        return "No user found with that passport number."
    phoneNumber = users[0]['phone_number']
    age = users[0]['age']
    gender = users[0]['gender']
    nationality = users[0]['NATIONALITY']
    address = users[0]['address']
    firstName = users[0]['first_Name']
    lastName = users[0]['last_Name']
    return render_template('passenger.html',firstName=firstName,lastName=lastName,passportNumber=passportNumber, phoneNumber=phoneNumber, age=age, nationality=nationality, gender=gender, address=address)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)