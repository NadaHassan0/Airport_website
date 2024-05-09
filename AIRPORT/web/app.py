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


@app.route('/passengers', methods=['POST'], strict_slashes=False)
def signup():
    conn = get_db_connection()
    try:
        data = request.get_json()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Passenger (first_Name, last_Name, phone_number, age, gender, passportNumber, NATIONALITY, address , email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (data['firstName'], data['lastName'], data['phoneNumber'], data['age'], data['gender'], data['passportNumber'], data['nationality'], data['address'] , data['email']))
        conn.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        cursor.close()
        close_db_connection(conn)
    return jsonify(data), 200 
    

'''@app.route('/get_employee_data', methods=['POST'])
def get_employee_data():
    try:
        # Get employee ID from request body
        data = request.get_json()
        employee_id = data['employeeID']

        # Connect to database
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        # Execute query to fetch employee data
        cursor.execute("SELECT * FROM employees WHERE employee_ID = %s", (employee_id,))
        employee_data = cursor.fetchone()
        conn.commit()

        # Check if data found
        if employee_data is None:
            return jsonify({'error': 'No employee found with this ID'}), 404

        # Prepare response data
        response = {
            'success': True,
            'employee': {
                "name": employee_data['name'],
                "phone": employee_data['phone'],
                "employee_ID": employee_data['employee_ID'],
                "age": employee_data['age'],
                "department": employee_data['department'],
                "job_title": employee_data['job_title'],
                "hire_date": employee_data['hire_date'],
                "salary": employee_data['salary'],
                "email": employee_data['email']
            }
        }

    except Exception as e:
        return jsonify({'error': str(e)}), 400

    finally:
        cursor.close()
        close_db_connection(conn)

    return jsonify(response), 200


@app.route('/employees/<int:employee_ID', methods=['GET'])
def get_employees(employee_ID):
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM employees where employee_ID = %s", (employee_ID,))
        data = cursor.fetchall()
        if data is None:
            return jsonify({'error': 'No employee found with this ID'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        cursor.close()
        close_db_connection(conn)
    return jsonify(data), 200
'''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)