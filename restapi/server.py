from flask import Flask, request

app=Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method =="GET":
        return "login.html"
    else:
        pass

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return "register.html"
    else:
        pass

@app.post("/logout")
def logout():
    pass