import asyncio
import random

from database import session
from repository import BookRepository
from utils.database_gen import fake_generate_book
from schemas.books import SBookAdd


async def update_random_books(count: int = 5, delay_min: float = 0.1, delay_max: float = 1.0):
    async with session() as s:
        # получаем все НЕ удаленные книги
        books = await BookRepository.get_all_books(s)

        if not books:
            print("Нет книг для обновления")
            return

        # ограничиваем количество
        count = min(count, len(books))

        # выбираем случайные книги
        books_to_update = random.sample(books, k=count)

        for book in books_to_update:
            # генерируем новые данные
            new_data = fake_generate_book()

            # приводим к схеме
            book_schema = SBookAdd(**new_data)

            # обновляем
            await BookRepository.update_info(book.id, book_schema, s)

            delay = random.uniform(delay_min, delay_max)
            await asyncio.sleep(delay)


async def main():
    await update_random_books(count=10)


if __name__ == "__main__":
    asyncio.run(main())