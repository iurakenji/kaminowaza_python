from fastapi import FastAPI
from dotenv import load_dotenv
import config
from app.routers import users
from app.database.connection import engine
from app.models.user import Base as UserBase

load_dotenv()

UserBase.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
@app.get("/")
def read_root():
    return {"message": "Sim!"}