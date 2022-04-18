import requests
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="postgres",
                        host="127.0.0.1",
                        port="5433")

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username.strip() or not password.strip():
        return render_template('login.html')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    print(records)

    if not records:
        return render_template('login.html')

    return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])


if __name__ == '__main__':
    app.run()
