import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('try_flask_getData.html')

@app.route('/login', methods=['POST', 'GET']) #allow both GET and POST requests
def login():
    if request.method == 'POST':
        #user = request.form['nm']
        return redirect(url_for('success'))
    else:
        return render_template('login.html')
    
@app.route("/<usr>")
def usr():
    return render_template(profile.html )


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)