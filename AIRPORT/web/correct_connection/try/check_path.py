from flask import Flask, render_template, request
import os
app = Flask(__name__)

print(os.path.isfile('/home/goc/projects/airPort_DB/files /try/templates/submit.html'))  # Check if file exists

@app.route('/submit', methods=(['POST']))
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    job = request.form.get('job')
   
    return render_template("/submit.html", name=name, age=age, job=job)

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=5000, threaded=True)