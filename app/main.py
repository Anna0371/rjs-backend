from fastapi import FastAPI
from app.routers import terms

app = FastAPI(
    title="RJS Tech Terms API",
    description="Бэкенд для базы знаний технических терминов на РЖЯ",
    version="1.0.0"
)

# Подключаем роутер для терминов
app.include_router(terms.router)
import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)