from os import environ
import os
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine, SQLModel

# username=environ.get("POSTGRES_USER")
# password=environ.get("POSTGRES_PASSWORD")
# host=environ.get("POSTGRES_HOST")
# db=environ.get("POSTGRES_DB")
# database_url=f"postgresql://{username}:{password}@{host}:5432/{db}"

DATABASE_URL= os.getenv(
                "DATABASE_URL",
                "sqlite:///./dev.db"
                )

if not DATABASE_URL:
    raise RuntimeError("Database has been not set")

engine =create_engine(
                DATABASE_URL,    
                echo=True,
                connect_args={"check_same_thread": False}
                if DATABASE_URL.startswith("sqlite")
                else {}
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionType= Annotated[Session, Depends(get_session)]

