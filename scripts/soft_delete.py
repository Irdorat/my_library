import asyncio
import random

from database import session
from repository import BookRepository


async def soft_delete_random_books(count: int = 5, delay_min: float = 0.1, delay_max: float = 1.0):
    async with session() as s:
        # получаем все книги
        books = await BookRepository.admin_get_all_books(s)

        if not books:
            print("Нет книг для удаления")
            return

        # выбираем случайные книги
        books_to_delete = random.sample(books, k=min(count, len(books)))

        for book in books_to_delete:
            await BookRepository.delete_info(book.id, s)

            delay = random.uniform(delay_min, delay_max)
            await asyncio.sleep(delay)


async def main():
    await soft_delete_random_books(count=3)


if __name__ == "__main__":
    asyncio.run(main())