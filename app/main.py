from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth.routers import router as auth_router
# from app.screener.routers import router as screener_router
# from app.recommendation.routers import router as recommendation_router
# from app.portfolio.routers import router as portfolio_router
# from app.analysis.routers import router as analysis_router
# from app.websockets.routers import router as ws_router

import uvicorn
import os
from dotenv import load_dotenv

from app.database import Base, engine

# ------------------------------
# ✅ Load environment variables
# ------------------------------
load_dotenv()

# ------------------------------
# ✅ Read frontend host/port from .env (with defaults)
# ------------------------------
FRONTEND_PORT = os.getenv("FRONTEND_PORT", "5173")
FRONTEND_HOST = os.getenv("FRONTEND_HOST", "localhost")

# ------------------------------
# ✅ Create tables if they don't exist
# ------------------------------
Base.metadata.create_all(bind=engine)

# ------------------------------
# ✅ Initialize FastAPI app
# ------------------------------
app = FastAPI(title="VrindaIQ Backend")

# ------------------------------
# ✅ Enable CORS so frontend can call API
# ------------------------------
origins = [
    f"http://{FRONTEND_HOST}:{FRONTEND_PORT}",
    f"http://127.0.0.1:{FRONTEND_PORT}",
]

# Optional: allow all origins in development mode
if os.getenv("CORS_ALLOW_ALL", "false").lower() == "true":
    origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------
# ✅ Include routers
# ------------------------------
app.include_router(auth_router, prefix="/auth", tags=["auth"])
# app.include_router(screener_router, prefix="/screener", tags=["screener"])
# app.include_router(recommendation_router, prefix="/recommendation", tags=["recommendation"])
# app.include_router(portfolio_router, prefix="/portfolio", tags=["portfolio"])
# app.include_router(analysis_router, prefix="/analysis", tags=["analysis"])
# app.include_router(ws_router, prefix="/ws", tags=["websockets"])

# ------------------------------
# ✅ Run app
# ------------------------------
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
