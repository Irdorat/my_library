import asyncio
import random

from database import session
from models.books import Book
from utils.database_gen import fake_generate_book
from repository import BookRepository
from schemas.books import SBookAdd


async def seed_books(count: int = 100, delay_min: float = 0.1, delay_max: float = 1.0):
    async with session() as s:
        for _ in range(count):
            data = fake_generate_book()            
            book_schema = SBookAdd(**data)

            # используем repository (ВАЖНО)
            await BookRepository.add_book(book_schema, s)

            delay = random.uniform(delay_min, delay_max)
            await asyncio.sleep(delay)


async def main():
    await seed_books()


if __name__ == "__main__":
    asyncio.run(main())