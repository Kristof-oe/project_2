from fastapi import FastAPI
from app.api import health, tasks
from contextlib import asynccontextmanager
from app.db.session import create_db_and_tables



@asynccontextmanager
async def lifespan(_: FastAPI):
    create_db_and_tables()
    yield

app=FastAPI(lifespan=lifespan)
app.include_router(health.router)
app.include_router(tasks.router)