from pydantic import BaseModel

class TermBase(BaseModel):
    name: str
    description: str
    video_url: str

class TermCreate(TermBase):
    pass

class TermUpdate(TermBase):
    pass

class TermRead(TermBase):
    id: int

    class Config:
        orm_mode = True