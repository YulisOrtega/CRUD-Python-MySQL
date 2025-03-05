from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from config.db import SessionLocal
import crud.users
from auth import decode_access_token

security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    user = crud.users.get_user_by_email(db, email=payload.get("sub"))
    if user is None:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    return user