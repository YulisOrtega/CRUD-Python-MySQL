from jwt import encode, decode

def solicitar_token(dato:dict) -> str:
    token:str = encode(payload=dato, key='secret_key', algorithm='HS256')
    return token

def validar_token(token:str) -> dict:
    dato:dict = decode(token,key='secret_key', algorithms=['HS256'])
    return dato