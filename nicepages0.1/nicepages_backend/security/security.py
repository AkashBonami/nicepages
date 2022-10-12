import jwt

def encoder(password):
    token = jwt.encode({"some" :  password}, "secret" ,algorithm="HS256")
    return token

def decoder(encoded_pass):
    password = jwt.decode(encoded_pass, "secret", algorithms=["HS256"])
    return password

# print(encoder("12345"))
# print(decoder("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoiMTIzNDUifQ.ucprFjT61lMkJJjOkSuMmpj6t6GBZSwetLWcOoAH_vE"))