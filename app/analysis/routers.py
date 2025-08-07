from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.dependencies import get_current_user
from .models import News
from .schemas import NewsCreate, News
from .ai_utils import analyze_sentiment
from app.database import get_db
from auth.models import User

router = APIRouter()

@router.post("/sentiment")
def sentiment_analysis(news: NewsCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    sentiment = analyze_sentiment(news.content)
    db_news = News(title=news.title, content=news.content, sentiment=sentiment, user_id=current_user.id)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return News.from_orm(db_news)