from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.routers import router as auth_router
# from screener.routers import router as screener_router
# from recommendation.routers import router as recommendation_router
# from portfolio.routers import router as portfolio_router
# from analysis.routers import router as analysis_router
# from websockets.routers import router as ws_router

import uvicorn
import os
from dotenv import load_dotenv

from database import Base, engine

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
# Automatically allow both localhost and 127.0.0.1 for the given port
origins = [
    f"http://{FRONTEND_HOST}:{FRONTEND_PORT}",
    f"http://127.0.0.1:{FRONTEND_PORT}",
]

# Optional: allow all origins in development mode
if os.getenv("CORS_ALLOW_ALL", "false").lower() == "true":
    origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # Or ["*"] to allow all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],           # Allow all HTTP methods: GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],           # Allow all headers
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
    uvicorn.run(app, host="0.0.0.0", port=8000)
