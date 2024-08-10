from sqlalchemy.orm import Session
from app.users import models, schemas, auth

def create_user(db: Session, email: str, password: str) -> schemas.UserResponse:
    hashed_password = auth.get_password_hash(password)
    db_user = models.User(email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": str(db_user.id), "email": db_user.email}

def get_user(db: Session, email: str) -> schemas.UserResponse:
    return db.query(models.User).filter(models.User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email)
    if not user or not auth.verify_password(password, user.hashed_password):
        return False
    return user