from pydantic import BaseModel

class NewsCreate(BaseModel):
    title: str
    content: str

class News(BaseModel):
    id: int
    title: str
    content: str
    sentiment: str

    class Config:
        from_attributes = True
