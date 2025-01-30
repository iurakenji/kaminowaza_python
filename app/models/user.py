from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(30), nullable=False)
    email = Column(String(100), unique=True, nullable=False)