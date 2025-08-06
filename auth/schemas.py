from pydantic import BaseModel, EmailStr, constr
from typing import Optional


# ---------- Request Schema for Registration ----------
class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=50, strip_whitespace=True)
    email: EmailStr
    password: constr(min_length=6)
    full_name: constr(min_length=2, max_length=100, strip_whitespace=True)
    mobile: Optional[constr(pattern=r"^\+?\d{10,15}$")] = None
    experience_level: Optional[str] = "Beginner"
    investment_style: Optional[str] = "Long-term"
    preferred_market: Optional[str] = "Stocks"


# ---------- Response Schema for User ----------
class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    mobile: Optional[str]
    experience_level: str
    investment_style: str
    preferred_market: str

    class Config:
        from_attributes = True


# ---------- Token Schema ----------
class Token(BaseModel):
    access_token: str
    token_type: str
