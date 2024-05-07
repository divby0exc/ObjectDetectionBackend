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
    # If its not None we know the username exists in the db
    if user_from_db is None:
        return json.dumps({"msg":"Username or Password is incorrect"}) 
    # but ofc we still want to verify the pwd is correct
    verify_user_pwd=dec_pwd(user_from_req["password"],user_from_db["password"])
    # if its correct. send the jwt time to hold the session
    if verify_user_pwd:
        return json.dumps({"correct":"true", "time":10})
    else:
        return json.dumps({"Message":"Username or Password is incorrect"})


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