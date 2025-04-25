import os
from dotenv import load_dotenv
from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from models import *


load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

db_url_async = f"postgresql+asyncpg://{db_user}:{db_password}@localhost/{db_name}"

engine_async = create_async_engine(db_url_async)
SessionLocal_async = sessionmaker(
    bind=engine_async, class_=AsyncSession, expire_on_commit=False
)

async def init_db_async():
    async with engine_async.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
