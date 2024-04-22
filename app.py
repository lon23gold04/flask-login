from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    username = request.args.get("username")
    password = request.args.get("password")
    print(username)
    print(password)
    if username == None:
        return render_template("index.html")
    elif username == "admin" and password == "admin123":
        return "<h1>Admin</h1>"
    else:
        return "<h1>User unrecognised.</h1>"