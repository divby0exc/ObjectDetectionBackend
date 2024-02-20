import base64

enc = base64.b64encode(b"soi*(&*&%^cjhwdoij4903")

print(enc)

dec = base64.b64decode(enc)

print(dec)