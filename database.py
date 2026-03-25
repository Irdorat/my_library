#Создаем таблицу БД.
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from typing import Annotated
from fastapi import Depends

#Настройка URL для SQLite (асинхронный драйвер aiosqlite)
DATABASE_URL="sqlite+aiosqlite:///library.db"
#Создание движка
engine=create_async_engine(DATABASE_URL)
#Фабрика сессий
session=async_sessionmaker(engine, expire_on_commit=False)
#Базовый класс моделей
class Model(MappedAsDataclass, DeclarativeBase):
    pass
async def get_db():
    async with session() as s:
        yield s
#где SessionDep - асинхр. сессия для взаимодействия с БД, Depends - зависимость для получения сессии из get_db
SessionDep=Annotated[AsyncSession, Depends(get_db)]
