# REST API - my_library
FastAPI | SQLite | 

Библиотечная система, реализованная на FASTAPI с полным CRUD функционалом


<h1> Tech Stack <a href="#-tech-stack--"><img src="https://raw.githubusercontent.com/HighAmbition211/HighAmbition211/auxiliary/others/skill.gif" width="32"></a> </h1>

### Languages
<table>
  <tr>
    <td align="center" width="90">
      <a href="https://www.python.org/" target="_blank">
        <img alt="Python" width="45" height="45" src="https://raw.githubusercontent.com/HighAmbition211/HighAmbition211/auxiliary/languages/python.svg" />
      </a>
      <br><h4>Python</h4>
    </td>
    <td align="center" width="90">
      <a href="https://en.wikipedia.org/wiki/SQL" target="_blank">
        <img alt="SQL" width="45" height="45" src="https://www.svgrepo.com/show/331760/sql-database-generic.svg" />
      </a>
      <br><h4>SQL</h4>
    </td>
  </tr>
</table>

### Frameworks & Libraries
<table>
  <tr>
    <td align="center" width="90">
      <a href="https://fastapi.tiangolo.com/" target="_blank">
        <img alt="FastAPI" width="45" height="45" src="https://icon.icepanel.io/Technology/svg/FastAPI.svg" />
      </a>
      <br><h4>FastAPI</h4>
    </td>
    <td align="center" width="90">
      <a href="https://docs.pydantic.dev" target="_blank">
        <img alt="Pydantic" width="45" height="45" src="https://avatars.githubusercontent.com/u/116566593?s=200&v=4" />
      </a>
      <br><h4>Pydantic</h4>
    </td>
    <td align="center" width="90">
      <a href="https://www.sqlalchemy.org/" target="_blank">
        <img alt="SQLAlchemy" height="45" src="https://www.sqlalchemy.org/img/sqla_logo.png" />
      </a>
      <br><h4>SQLAlchemy</h4>
    </td>
        <td align="center" width="90">
      <a href="https://www.uvicorn.org/" target="_blank">
        <img alt="Uvicorn" height="45" src="https://raw.githubusercontent.com/encode/uvicorn/master/docs/uvicorn.png" />
      </a>
      <br><h4>Uvicorn</h4>
    </td>
  </tr>
</table>

### Databases
<table>
  <tr>
    <td align="center" width="90">
      <a href="https://www.sqlite.org/" target="_blank">
        <img alt="SQLite" width="45" height="45" src="https://www.sqlite.org/images/sqlite370_banner.gif" />
      </a>
      <br><h4>SQLite</h4>
    </td>
  </tr>
</table>

---

#Структура проекта
```
|-src/
||-models/ #SQLAlchemy модель
||-routers/ #Маршруты API
||-schemas/ #Pydantic схемы
||-scipts/ #изменение данных в бд скриптом 
||-utils/ #фейковая генерация БД
||-database.py #Подключение к БД
||-main.py #Точка входа FASTAPI
||-repository.py #Работа с данными
```
# Начало работы
```
1) Клонировать репозиторий
git clone https://github.com/Irdorat/my_library
cd my_library

2) Создать виртуальное окружение (из файла req*.txt)

python -m venv venv

venv\Scripts\activate

3) Установить зависимости

pip install -r requirements.txt

4) Запустить main.py

uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=4)

```

# SWAGGER UI

Swagger UI документация: http://0.0.0.0:8000/docs

ReDoc документация: http://0.0.0.0:8000/redoc

# API Endpoints

<table>
  <tr>
    <th>Метод</th>
    <th>Endpoint</th>
    <th>Описание</th>
    <th>Статус</th>
  </tr>
  <tr>
    <td>POST</td>
    <td>/books</td>
    <td>Добавить данные в БД</td>
    <td>201_CREATED</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/books</td>
    <td>Получить данные в БД (is_deleted=False)</td>
    <td>200_OK</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/books/admin</td>
    <td>Получить все данные в БД (is_deleted=TRUE)</td>
    <td>200_OK</td>
  </tr>
    <tr>
    <td>GET</td>
    <td>/books/{book_id}</td>
    <td>Получить данные в БД по ID книги</td>
    <td>200_OK<br>404_NOT_FOUND</td>
  </tr>
    </tr>
    <tr>
    <td>PATCH</td>
    <td>/books/{book_id}</td>
    <td>Обновить данные в БД по ID книги</td>
    <td>200_OK<br>404_NOT_FOUND</td>
  </tr>
    </tr>
    </tr>
    <tr>
    <td>DELETE</td>
    <td>/books/{book_id}</td>
    <td>Удалить данные в БД по ID книги(soft delete)</td>
    <td>204_NO_CONTENT<br>404_NOT_FOUND</td>
  </tr>
    <tr>
    <td>DELETE</td>
    <td>/books/admin/{book_id}</td>
    <td>Удалить данные в БД по ID книги (hard delete)</td>
    <td>204_NO_CONTENT<br>404_NOT_FOUND</td>
  </tr>
</table>