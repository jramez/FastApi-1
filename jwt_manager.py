from jwt import encode, decode

def create_token(data:dict):
    token:str = encode(payload=data,key="mi_clave_secreta",algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="mi_clave_secreta",algorithms=['HS256'])
    return data