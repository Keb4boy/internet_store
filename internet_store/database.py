from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

engine: AsyncEngine = create_async_engine(f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
async_session: AsyncSession = sessionmaker(engine, class_= AsyncSession)