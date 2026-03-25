from unittest import result

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.books import Book
from schemas.books import SBookAdd

class BookRepository:
    #Добавить книгу в БД
    @classmethod
    async def add_book(cls,
                       book:SBookAdd,
                       session: AsyncSession) -> Book:
        #проверяем есть ли книга с таким же названием и автором или есть с флагом удалена, чтобы можно было вернуть ее обратно
        query=select(Book).where((Book.title==book.title)&(Book.author==book.author))
        result=await session.execute(query)
        existing_book=result.scalar_one_or_none()
        if existing_book:
            if existing_book.is_deleted:
                existing_book.is_deleted=False
                await session.commit()
                await session.refresh(existing_book)
                return existing_book
            else:
                return existing_book
        #превращаем данные в словрь
        book_dict=book.model_dump()
        #создаем объект модели
        # ** - это распаковка словаря
        new_book=Book(**book_dict)
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book
    
    #Получить все книги из БД (за исключеним удаленных)
    @classmethod
    async def get_all_books(cls, session: AsyncSession):
        query = select(Book).where(Book.is_deleted==False)
        result = await session.execute(query)
        books = result.scalars().all()
        return books
    
    #Получить ВСЕ книги из БД (admin)
    @classmethod
    async def admin_get_all_books(cls, session:AsyncSession):
        query=select(Book)
        result=await session.execute(query)
        books=result.scalars().all()
        return books
    
    #Получить книги по ID (за исключением удаленных)
    @classmethod
    async def get_books_by_id(cls, book_id: int,session:AsyncSession):
        query=select(Book).where((Book.id==book_id)&(Book.is_deleted==False))
        result=await session.execute(query)
        book=result.scalar_one_or_none()
        return book
    
    #Обновить книгу по ID (за исключением удаленных)
    @classmethod
    async def update_info(cls, book_id: int, book: SBookAdd, session:AsyncSession):
        query=select(Book).where((Book.id==book_id)&(Book.is_deleted==False))
        result=await session.execute(query)
        upd_book=result.scalar_one_or_none()
        if not upd_book:
            return None
        update_info=book.model_dump(exclude_unset=True)
        query=update(Book).where(Book.id==book_id).values(**update_info)
        await session.execute(query)
        await session.commit()
        await session.refresh(upd_book)
        return upd_book
    
    #Удалить книгу по ID(soft delete)
    @classmethod
    async def delete_info(cls, book_id: int, session:AsyncSession):
        query = select(Book).where((Book.id == book_id) & (Book.is_deleted == False))
        result = await session.execute(query)
        del_book = result.scalar_one_or_none()
        if not del_book:
            return None
        del_book.is_deleted = True

        await session.commit()
        await session.refresh(del_book)
        return del_book
    
    #Hard delete книги по ID(admin only)
    @classmethod
    async def admin_delete_info(cls, book_id: int, session:AsyncSession):
        query=select(Book).where(Book.id==book_id)
        result=await session.execute(query)
        exists=result.scalar_one_or_none()
        if not exists:
            return None
        del_query=delete(Book).where(Book.id==book_id)
        await session.execute(del_query)
        await session.commit()
        return True