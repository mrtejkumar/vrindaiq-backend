from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    sentiment = Column(String)  # AI-generated
    user_id = Column(Integer, ForeignKey("users.id"))