# backend/app/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.api.users import users_routes
from prisma import Prisma

# Initialize Prisma client
prisma = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    try:
        yield
    finally:
        await prisma.disconnect()


app = FastAPI(lifespan=lifespan, title=settings.PROJECT_NAME)

app.include_router(users_routes.public_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
