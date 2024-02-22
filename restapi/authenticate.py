import jwt
import bcrypt

# Obviously a bad idea to have this public but anywho, local
SIGN_KEY="\x1e\x82#?\xddP\xb5\x8c\xc1\x7f;\xa8\xa6\xcf\xe1<\xcf\xde\xb48\xe2\x8d\x8d\xfc7\xf1\xb8\xbb\xfb\xea!\xc4"

def sign_jwt(user_obj:dict):
    # Add exp time
    encoded_jwt = jwt.encode({"dani":"123456"}, SIGN_KEY, algorithm="HS256")
    return encoded_jwt

# Need to return an exp time to the UI
def verify_token(token):
    decoded=jwt.decode(token,SIGN_KEY,algorithms=["HS256"])

# This will be used with create_user func to be saved in db
def crypt_pwd(pwd:str):
    crypted=bcrypt.hashpw(bytes(pwd.encode("utf-8")), bcrypt.gensalt())
    return crypted

# Hashed arg is not suppose to be there.
# Need to implement the func from db instead
def dec_pwd(pwd:str, hashed:bytes):
    decrypted=bcrypt.checkpw(bytes(pwd.encode("utf-8")), hashed)#Call the function to fetch the hash from db
    return decrypted