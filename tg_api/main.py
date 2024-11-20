from contextlib import asynccontextmanager
from fastapi_admin.app import app as admin_app
from fastapi import FastAPI
from database import create_tables, delete_tables

from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    await delete_tables()


app = FastAPI(lifespan=lifespan)
app.mount("/admin", admin_app)

app.include_router(tasks_router)
