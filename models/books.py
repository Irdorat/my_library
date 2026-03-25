from sqlalchemy.orm import Mapped, mapped_column
from database import Model

class Book(Model):
    __tablename__="library"
    id: Mapped[int]=mapped_column(primary_key=True, init=False)
    category: Mapped[str]
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int]
    pages: Mapped[int]
    is_read: Mapped[bool]=mapped_column(default=False)
    is_deleted: Mapped[bool]=mapped_column(default=False)