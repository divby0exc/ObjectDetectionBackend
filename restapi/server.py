from flask import Flask

app=Flask(__name__)

@app.post("/login")
def login():
    pass
