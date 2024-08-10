from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(String, default=datetime.now())
