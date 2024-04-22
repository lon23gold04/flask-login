from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    username = request.args.get("username")
    if username == None:
        print(username)
        return render_template("index.html")
    elif username == "admin":
        return "<h1>Admin</h1>"
    else:
        return "<h1>User does not exist.</h1>"