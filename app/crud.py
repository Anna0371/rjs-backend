from sqlalchemy.orm import Session
from app.models import Term

# Функция для добавления термина
def create_term(db: Session, name: str, description: str, video_url: str):
    db_term = Term(name=name, description=description, video_url=video_url)
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term

# Функция для обновления термина
def update_term(db: Session, term_id: int, updated_data: dict):
    term = db.query(Term).filter(Term.id == term_id).first()
    if term:
        for key, value in updated_data.items():
            setattr(term, key, value)
        db.commit()
        db.refresh(term)
        return term
    return None
