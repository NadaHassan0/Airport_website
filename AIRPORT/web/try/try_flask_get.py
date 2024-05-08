from flask import Flask, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/passengers', methods=['GET'])
def get_passengers():
    db_connection = pymysql.connect(
        host="0.0.0.0",
        user="root",
        password="NO",
        database="Airborne"
    )
    cursor = db_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Passenger")
    rows = cursor.fetchall()
    cursor.close()
    db_connection.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)