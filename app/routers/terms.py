from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from app import crud, models, schemas
from app.database import get_db

router = APIRouter()

# Создание термина
@router.post("/terms/")
def create_term(name: str, description: str, video_url: str, db: Session = Depends(get_db)):
    return crud.create_term(db=db, name=name, description=description, video_url=video_url)

# Получение термина по ID
@router.get("/terms/{term_id}")
def get_term(term_id: int, db: Session = Depends(get_db)):
    return db.query(models.Term).filter(models.Term.id == term_id).first()

# Поиск терминов по названию (LIKE) + отладка
@router.get("/terms")
def search_terms(query: Optional[str] = None, db: Session = Depends(get_db)):
    try:
        terms_query = db.query(models.Term)
        if query:
            terms_query = terms_query.filter(models.Term.name.ilike(f"%{query}%"))
        return terms_query.all()
    except Exception as e:
        return {"error": str(e)}

# Обновление термина
@router.put("/terms/{term_id}")
def update_term(term_id: int, term: schemas.TermUpdate, db: Session = Depends(get_db)):
    updated = crud.update_term(db, term_id, term.dict())
    if updated:
        return updated
    return {"message": "Term not found"}

# Удаление термина
@router.delete("/terms/{term_id}")
def delete_term(term_id: int, db: Session = Depends(get_db)):
    term = db.query(models.Term).filter(models.Term.id == term_id).first()
    if term:
        db.delete(term)
        db.commit()
        return {"message": "Term deleted successfully"}
    return {"message": "Term not found"}