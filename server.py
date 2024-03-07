from create_user import save
from flask import Flask, request
from authenticate import sign_jwt, dec_pwd
from user import User

app=Flask(__name__)

@app.post("/login")
def login():
    user_obj:User = request.json
    if user_obj

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return "register.html"
    else:
        user=request.json
        save(user.get_username(),user.get_pwd())
        

@app.post("/logout")
def logout():
    pass

@app.get("/connected")
def check():
    return {"is_connected":"true"}

app.run(debug=True)