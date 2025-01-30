from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    email: str

class UserUpdate(BaseModel):
    nome: str
    email: str

class UserResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True