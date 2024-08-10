from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.users.schemas import UserCreate, UserResponse
from app.users.crud import create_user, get_user, authenticate_user
from app.users.auth import generate_access_token

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.post("/register/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
  email_clean = user.email.strip().lower()
  existing_user = get_user(db, email_clean)
  if existing_user:
    raise HTTPException(status_code=400, detail="Email already registered")
  return create_user(db, email_clean, user.password)

@router.post("/login/")
def login(user: UserCreate, db: Session = Depends(get_db)):
  user = authenticate_user(db, user.email, user.password)
  if not user:
    raise HTTPException(status_code=401, detail="Invalid credentials")
  token = generate_access_token(user, timedelta(minutes=30))
  return {'access_token': token, 'token_type': 'bearer'}