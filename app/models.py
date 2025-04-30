from sqlalchemy import Column, Integer, String
from app.database import Base

class Term(Base):
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    video_url = Column(String)