from database import save, fetch_user, user_exists
from flask import Flask, request
from authenticate import sign_jwt, dec_pwd
from user import User
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


@app.post("/register")
def register():
        user=request.json
        if user_exists(user["username"]) is False:
            new_user = User(user["username"], user["password"])
            save(new_user)
            return json.dumps({"Msg":"User registered "+user["username"]})
        else:
             return json.dumps({"Msg":"Username alreday exists"})
        

@app.post("/logout")
def logout():
    pass

@app.get("/connected")
def check():
    return {"is_connected":"true"}

app.run(debug=True)