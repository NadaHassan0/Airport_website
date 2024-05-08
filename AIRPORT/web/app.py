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
def add_passenger():
    conn = get_db_connection()
    try:
        data = request.get_json()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Passenger (name, age, email) VALUES (%s, %s, %s)",
                       (data['name'], data['age'], data['email']))
        conn.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        cursor.close()
        close_db_connection(conn)
    return jsonify(data), 200

@app.route('/passengers/<int:passportID>', methods=['GET'])
def get_profile(passportID):
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM passengers WHERE passportID = %s", (passportID,))
        data = cursor.fetchone()
        if data is None:
            return jsonify({'error': 'No profile found with this ID'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        cursor.close()
        close_db_connection(conn)
    return jsonify(data), 200

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)