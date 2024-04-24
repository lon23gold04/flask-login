from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(username)
        print(password)
        if username == "admin" and password == "admin123":
            return "<h1>Admin</h1>"
        else:
            return "<h1>User unrecognised.</h1>"