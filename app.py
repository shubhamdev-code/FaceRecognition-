import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_folder='static')

try:
    db = mysql.connector.connect(
      host='localhost',
      user='root',
      password='Shubham@1210',
      database='flask_app'
    )
    print("connection successful")
except:
    print("Eroor")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(query, values)

    user = cursor.fetchall()

    if user:
        return redirect('/welcome')
    else:
        return redirect('/notfound')

@app.route('/welcome')
def welcome():
    return 'Welcome!'


@app.route('/notfound')
def notfound():
    return "User not found"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
