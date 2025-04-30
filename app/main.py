from fastapi import FastAPI
from app.routers import terms

app = FastAPI(
    title="RJS Tech Terms API",
    description="Бэкенд для базы знаний технических терминов на РЖЯ",
    version="1.0.0"
)

# Подключаем роутер для терминов
app.include_router(terms.router)