from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate, Token
from .dependencies import get_password_hash, verify_password, create_access_token, get_current_user

from database import get_db
# // Remove: from .schemas import User  # Add this if not already imported

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check username
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(
            status_code=400,
            detail={"field": "username", "message": "Username already exists"}
        )

    # Check email format
    if "@" not in user.email:
        raise HTTPException(
            status_code=400,
            detail={"field": "email", "message": "Invalid email format"}
        )

    # Check email uniqueness
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(
            status_code=400,
            detail={"field": "email", "message": "Email already registered"}
        )

    # Optional: Check mobile
    if user.mobile and db.query(User).filter(User.mobile == user.mobile).first():
        raise HTTPException(
            status_code=400,
            detail={"field": "mobile", "message": "Mobile number already registered"}
        )

    # Create new user
    hashed_password = get_password_hash(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name or "Guest",
        mobile=user.mobile
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg": "User registered successfully"}


@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/protected-test")
def protected_test(current_user: User = Depends(get_current_user)):
    return {"msg": f"Hello, {current_user.username}"}