from fastapi import FastAPI
from app.routes.ops import router as ops_router
from app.routes.client import router as client_router
from app.database import engine, Base

app = FastAPI()

# routers
app.include_router(ops_router, prefix="/ops", tags=["Ops User"])
app.include_router(client_router, prefix="/client", tags=["Client User"])

# Database
Base.metadata.create_all(bind=engine)


