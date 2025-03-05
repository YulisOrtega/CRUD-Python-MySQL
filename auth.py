import jwt
from datetime import datetime, timedelta
from typing import Optional


SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    # Copia los datos proporcionados
    to_encode = data.copy()
    # Si se proporciona un tiempo de expiración, se utiliza; de lo contrario, se usa el tiempo por defecto
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Añade la información de expiración a los datos
    to_encode.update({"exp": expire})
    # Codifica los datos en un token JWT
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        # Decodifica el token JWT utilizando la clave secreta y el algoritmo especificado
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        # Retorna None si el token ha expirado
        return None
    except jwt.InvalidTokenError:
        return None