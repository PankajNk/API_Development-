from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/ops/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        print(f"Token received: {token}")  # Log the token
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        print(f"Decoded payload: {payload}")  #decoded payload
        
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid credentials: Missing subject")
        
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials: User not found")
        
        print(f"User found: {user.username}, Role: {user.role}")  #  user info
        return user
    except JWTError as e:
        print(f"Token validation error: {e}")  
        raise HTTPException(status_code=401, detail="Invalid token")

def role_required(role: str):
    def role_checker(user: User = Depends(get_current_user)):
        print(f"Checking role for user: {user.username}, Required role: {role}")  
        if user.role != role:
            print(f"Unauthorized access attempt by user: {user.username}, Role: {user.role}")  
            raise HTTPException(status_code=403, detail="Unauthorized")#error 
        return user
    return role_checker
