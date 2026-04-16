from fastapi import FastAPI
from app.routers import router

app = FastAPI(title="Planner")
app.include_router(router)