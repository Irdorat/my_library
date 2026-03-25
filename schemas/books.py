from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

#Получаем статичнское значение текущего года для валидации поля Year
now=datetime.now()

#Схема для создания и обновления новой книги
class SBookAdd(BaseModel):
    category: str | None = Field(
        default=None, 
        title="Категория книги", 
        description="Здесь можно добавить категорию книги: Фантастика, Научная литература, Роман и т.д."
        )
    title: str = Field(...,
                       title="Название книги",
                       description="Здесь НУЖНО добавить название произведения",
                       min_length=5
                       )
    author: str = Field(
        title="ФИО автора",
        description="Здесь НУЖНО добавить ФИО автора",
        min_length=5
        )
    year: int = Field(
        title="Год книги",
        description="Здесь НУЖНО добавить название произведения",
        ge=0,
        le=now.year
        )
    pages: int = Field(
        title="Количество страниц в произведении",
        description="Здесь НУЖНО добавить количество страниц БОЛЬШЕ 10",
        ge=10
        )
    is_read: bool = Field(
        default=False,
        title="Прочитано ли произведение",
        description="Здесь можно указать, прочитано ли произведение (по умолчанию False)")
    
#Схема для возврата книги клиенту
class SBook(SBookAdd):
    id: int = Field(title="ID книги в БД",
                    description="Уникальный ID номер книги в БД")
    #Это нужно для того, чтобы Pydantic мог создавать объекты SBook из объектов SQLAlchemy, возвращаемые с БД. 
    model_config=ConfigDict(from_attributes=True)