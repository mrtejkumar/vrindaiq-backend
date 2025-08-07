# ⚡ VrindaIQ Backend

FastAPI-based backend service for the **VrindaIQ** platform — an intelligent trading assistant powered by AI and Angel One Smart APIs.

---

## ✨ Features

- ✅ **Modular FastAPI Architecture**
- 🔐 **JWT Authentication**
- 📊 **AI-driven Stock Analysis**
- 🧠 **Trading Recommendations (Coming Soon)**
- 📡 **Real-time WebSocket Updates**
- 🔗 **Angel One SmartAPI Integration**
- 🌐 **Secure CORS Middleware**
- 🛠️ **Environment-Based Config with `.env`**

---

## 📁 Project Structure

vrindaiq-backend/
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── database.py # SQLAlchemy setup
│ ├── config.py # .env-based configuration
│ ├── core/ # Auth & constants
│ ├── common/ # Shared utilities
│ ├── auth/ # Auth (JWT, models, routes)
│ ├── analysis/ # AI utils, analysis routes
│ ├── websockets/ # Real-time connections
│ └── third_party/
│ └── angelone/ # Angel One integration
├── angelone/ # Raw token storage, SDKs etc.
├── env/
│ └── .env # Local environment variables
├── requirements.txt # Python dependencies
└── README.md # You're reading it!

yaml
Copy
Edit

---

## 🧭 Step-by-Step Setup Guide

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/yourusername/vrindaiq-backend.git
cd vrindaiq-backend
✅ 2. Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv env
# Activate:
source env/bin/activate         # macOS/Linux
env\Scripts\activate            # Windows
✅ 3. Install Python Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ 4. Create a .env File
Create .env inside env/ or project root:

ini
Copy
Edit
# .env

# CORS / Frontend
FRONTEND_HOST=localhost
FRONTEND_PORT=5173
CORS_ALLOW_ALL=true

# Security
SECRET_KEY=your-very-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database
DATABASE_URL=sqlite:///./vrindaiq.db  # Change if using PostgreSQL
✅ 5. Run the Backend Server
bash
Copy
Edit
uvicorn app.main:app --reload
API: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

🧪 Development Tips
✅ Use .env to switch between development and production.

🧠 Any AI utilities should go inside analysis/ai_utils.py.

🔐 JWT auth-related logic lives in core/security.py.

⚙️ Add new routers in main.py using:

python
Copy
Edit
from app.newmodule.api import router as newmodule_router
app.include_router(newmodule_router, prefix="/newmodule", tags=["newmodule"])
🗺️ Planned / Future Additions
Feature	Status
✅ Authentication	Done
🧠 AI Recommendation Engine	Coming Soon
📈 Screener Module	In Progress
🧳 Portfolio Tracker	Planned
🧪 Unit Tests	Planned
🔄 Token Refresh	Planned
☁️ Docker Support	Planned
📦 PostgreSQL Option	Optional

🤝 Contributing
Pull requests are welcome. Please follow the structure and naming conventions.

To add a new module:

Create a new folder under app/

Add models.py, schemas.py, api.py, utils.py (as needed)

Register its router in main.py

🛡️ License
MIT License © 2025 VrindaIQ

📬 Contact
For bugs, feature requests, or contributions, feel free to reach out via GitHub or your-email@example.com