from create_user import save
from flask import Flask, request
from authenticate import sign_jwt, dec_pwd
from user import User
from read_user import fetch_user
import json

app=Flask(__name__)

@app.post("/login")
def login():
    user_from_req = request.json
    user_from_db = fetch_user(user_from_req["username"])
    verify_user_pwd=dec_pwd(user_from_req["password"],user_from_db["password"])
    if verify_user_pwd:
        return json.dumps({"Msg":"Password was a match"})
    else:
        return json.dumps({"Msg":"Username or Password is incorrect"})


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