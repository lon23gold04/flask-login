from flask import Flask, render_template, request
import sqlite3 as sql

DB_PATH = "database.db"

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        with open("users.txt", "r") as f:
            iterable = iter([part for part in f.read().split("\n") if part != ''])
            creds = dict(zip(iterable, iterable))
            print(creds)
            if username in creds:
                if password == (real_pass := creds[username]):
                    return f"Recoginsed user: {username} with password: {real_pass}"
            return "<h1>User unrecognised.</h1>"

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        print(username)
        print(password)
        print(confirm_password)
        if password == confirm_password:
            conn = sql.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("""INSERT INTO user (username, password)
                        VALUES (?, ?)""",
                        (username, password))
            conn.commit()
            conn.close()
            return "Successfully registered."
        else:
            return "Passwords do not match"