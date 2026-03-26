---
title: Readme
marimo-version: 0.21.1
---

# my_library
Библиотечная система, реализованная на FASTAPI с полным CRUD функционалом

# начало работы
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

# SWAGGER UI

Swagger UI документация: http://0.0.0.0:8000/docs

ReDoc документация: http://0.0.0.0:8000/redoc

# API Endpoints

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
  </tr>
</table>

### Databases
<table>
  <tr>
    <td align="center" width="90">
      <a href="https://www.sqlite.org/" target="_blank">
        <img alt="SQLite" width="45" height="45" src="https://raw.githubusercontent.com/HighAmbition211/HighAmbition211/auxiliary/databases/postgres.svg" />
      </a>
      <br><h4>PostgreSQL</h4>
    </td>
  </tr>
</table>

```python {.marimo}
import marimo as mo
```

```python {.marimo hide_code="true"}
mo.md(r"""

""")
```