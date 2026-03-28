
from jose import JWTError ,jwt
ALGORITHM = "HS256"

def create_access_token(data: dict, secret_key: str):
    return jwt.encode(data, secret_key, algorithm=ALGORITHM)

def decode_access_token(token: str, secret_key: str):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        print("JWT Decode Error:", e)
        return None
    
#  **************TEST**************

SECRET_KEY = "my_secret_key"

token = create_access_token({"user_id": 123}, SECRET_KEY)
print("TOKEN:", token)

decode = decode_access_token(token, SECRET_KEY)
print("DECODE DATA:", decode)