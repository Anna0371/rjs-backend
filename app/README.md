# RJS Tech Terms API

Бэкенд для базы знаний технических терминов на русском жестовом языке (РЖЯ).

---

## 🚀 Возможности

- 📄 Создание, просмотр, редактирование и удаление терминов
- 🔍 Поиск терминов по названию (LIKE-запрос)
- 💾 Работа с PostgreSQL через SQLAlchemy
- ⚙️ Полноценный REST API с документацией по адресу `/docs`

---

## ⚙️ Технологии

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Pydantic**
- **Uvicorn**

---

## 📂 Структура проекта

```bash
Backend/
├── app/
│   ├── main.py             # Точка входа (FastAPI-приложение)
│   ├── database.py         # Подключение к базе данных
│   ├── models.py           # Модель таблицы Term
│   ├── crud.py             # CRUD-логика
│   ├── schemas.py          # Pydantic-схемы
│   └── routers/
│       └── terms.py        # Роутеры (маршруты) для терминов
├── requirements.txt        # Список библиотек
├── README.md               # Инструкция