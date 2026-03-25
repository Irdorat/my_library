from contextlib import asynccontextmanager
from database import engine, Model
from fastapi import FastAPI
from routers.books import router as book_router
from datetime import datetime
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    #Создаем таблицы при запуске приложения
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
    
    start_time=datetime.now()
    print(f'БД готова к работе')
    print(f'Время запуска сервера: {start_time}')

    yield

    print(f'Выключение сервера')
    print(f'Сервер проработал: {datetime.now()-start_time}')

app=FastAPI(lifespan=lifespan)
app.include_router(book_router)

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=4)
