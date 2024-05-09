from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process_data', methods=['POST'])
def process_data():
    if request.method == 'POST':
        data = request.get_json()  # Access JSON data from request

        if data is None:
            return 'Error: No JSON data found in request.', 400  # Handle missing data

        try_data = data['try']

        # ... (your data processing logic)

        # Return a variable to be displayed in display.html (optional)
        processed_data = try_data.upper()  # Example processing (make changes)

        return render_template('display.html', variable=processed_data)  # Render display.html

if __name__ == '__main__':
    app.run(debug=True)
