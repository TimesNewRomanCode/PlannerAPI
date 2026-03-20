from fastapi import FastAPI
from app.router import router

app = FastAPI(title="name")
app.include_router(router)