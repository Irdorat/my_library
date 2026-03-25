from fastapi import APIRouter, HTTPException, status
from schemas.books import SBookAdd, SBook
from database import SessionDep
from repository import BookRepository

router=APIRouter(
    prefix="/books", 
    tags=["Книги"]
    )

@router.post("", status_code=status.HTTP_201_CREATED, response_model=SBook)
async def post_book(book:SBookAdd, session: SessionDep):
    task=await BookRepository.add_book(book, session)
    return task

@router.get("", status_code=status.HTTP_200_OK, response_model=list[SBook])
async def get_all_books(session: SessionDep):
    books=await BookRepository.get_all_books(session)
    return books

#admin only
@router.get("/admin", status_code=status.HTTP_200_OK, response_model=list[SBook])
async def admin_get_all_data(session: SessionDep):
    data=await BookRepository.admin_get_all_books(session)
    return data

@router.get("/{book_id}", status_code=status.HTTP_200_OK, response_model=SBook)
async def get_book_by_id(book_id: int, session: SessionDep):
    book=await BookRepository.get_books_by_id(book_id, session)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книги по этому ID не найдено")
    return book

@router.patch("/{book_id}", status_code=status.HTTP_200_OK, response_model=SBook)
async def update_book(book_id: int, book:SBookAdd, session: SessionDep):
    update_book=await BookRepository.update_info(book_id, book, session)
    if not update_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книги по этому ID не найдено")
    return update_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def del_book(book_id: int, session: SessionDep):
    delete_book=await BookRepository.delete_info(book_id, session)
    if not delete_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книги по этому ID не найдено")
    return None

@router.delete("/admin/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def admin_del_book(book_id: int, session:SessionDep):
    delete_book=await BookRepository.admin_delete_info(book_id, session)
    if not delete_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="У тебя доступ к БД, а ты пишешь хуйню. Книги по этмоу ID нет")
    return None