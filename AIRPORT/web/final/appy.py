from flask import Flask,render_template, request
from flask_cors import CORS
import pymysql
import werkzeug

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

temp = None

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
    global temp
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
    temp = passportNumber
    return render_template('passenger.html',firstName=firstName,lastName=lastName,passportNumber=passportNumber, phoneNumber=phoneNumber, age=age, nationality=nationality, gender=gender, address=address)


@app.route('/signup', methods=['POST'])
def signup():
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    phoneNumber = request.form.get('phoneNumber')
    age = request.form.get('age')
    email = request.form.get('email')
    gender = request.form.get('gender')
    passportNumber = request.form.get('passportNumber')
    nationality = request.form.get('nationality')
    address = request.form.get('address')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Passenger (passportNumber, NATIONALITY,age,gender,phone_number,email,address,first_Name,last_Name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (passportNumber,nationality,age,gender,phoneNumber,email,address,firstName,lastName))
    conn.commit()
    close_db_connection(conn)
    return render_template('login.html')

@app.route('/emp', methods=['POST'])
def emp():
    empId = request.form.get('empId')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employee where employee_ID = %s", (empId,))
    users = cursor.fetchall()
    close_db_connection(conn)
    if not users:
        return "No Employee found with that ID."
    name = users[0]['Name']
    phoneNumber = users[0]['Phone_number']
    age = users[0]['Age']
    department = users[0]['Department']
    jobTitle = users[0]['Job_Title']
    salary = users[0]['Salary']
    email = users[0]['Email']
    hireDate = users[0]['Hire_date']
    return render_template('employee.html',empId=empId,name=name,phoneNumber=phoneNumber,age=age,department=department,jobTitle=jobTitle,salary=salary,email=email,hireDate=hireDate)


@app.route('/book', methods=['POST'])
def book():
    return render_template("submit.html")


@app.route('/flight', methods=['POST'])
def flight():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        date= request.form.get('arrivalAirport')
        print(date)
        cursor.execute("SELECT * FROM Flight where Arrival_Airport = %s", (date,))
        flights = cursor.fetchall()
        if not flights:
            return "No Flight found with that date."
        close_db_connection(conn)
        return render_template('book.html',flights=flights)
    except Exception as e:
        print(e)
        return render_template('error.html', error=str(e))


@app.route('/booking-details', methods=['POST'])
def booked():
    global temp
    try:
        data = request.form
        print(data)
        data = list(data.values())
        #data = data[0].split(',')
        #print(data)
        conn = get_db_connection()
        cursor = conn.cursor()
        print(temp)
        print(data)
        if not temp:
            return "Please login first"
        cursor.execute("UPDATE Passenger SET flight = %s WHERE passportNumber = %s", (data, temp,))
        conn.commit()
        close_db_connection(conn)
        return ("Flight booked successfully")
    except Exception as e:
        print(e)
        return render_template('error.html', error=str(e)), 500


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, werkzeug.exceptions.HTTPException):
        return e

    # handling non-HTTP exceptions only
    print(e)
    return render_template('error.html', error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)