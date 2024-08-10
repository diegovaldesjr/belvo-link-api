from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    email: str

    class Config:
        json_schema_extra = {'example': {'id': 'dwada', 'email': 'user@email.com'}}

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        json_schema_extra = {'example': {'access_token': 'mgK', 'token_type': 'bearer'}}
