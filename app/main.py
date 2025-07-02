from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.auth import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"mensagem": "API de autenticação pronta para uso!"}

app.include_router(auth_router)