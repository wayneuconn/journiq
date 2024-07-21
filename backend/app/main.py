# backend/app/main.py
from fastapi import FastAPI
# from app.routes import api
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# app.include_router(api.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
