from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from app.models import User
from app.encryption import encrypt_field
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os

router = APIRouter()
security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY", "demo-secret-key")
ALGORITHM = "HS256"

@router.post("/register")
def register(user_data: dict):
    # Demo registration logic
    return {"message": "User registered successfully", "user_id": 1}

@router.post("/login")
def login(credentials: dict):
    # Demo login logic
    token = jwt.encode(
        {"sub": "demo@example.com", "exp": datetime.utcnow() + timedelta(hours=24)},
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return {"access_token": token, "token_type": "bearer"}

@router.post("/logout")
def logout():
    return {"message": "Logged out successfully"}
