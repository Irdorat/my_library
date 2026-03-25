import asyncio
import random

from database import session
from repository import BookRepository


async def hard_delete_random_books(count: int = 30, delay_min: float = 0.1, delay_max: float = 1.0):
    async with session() as s:
        # берем ВСЕ книги (включая удалённые)
        books = await BookRepository.admin_get_all_books(s)

        if not books:
            print("Нет книг для удаления")
            return

        # выбираем случайные книги
        books_to_delete = random.sample(books, k=min(len(books), len(books)))

        for book in books_to_delete:
            await BookRepository.admin_delete_info(book.id, s)

            delay = random.uniform(delay_min, delay_max)
            await asyncio.sleep(delay)


async def main():
    await hard_delete_random_books()


if __name__ == "__main__":
    asyncio.run(main())