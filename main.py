from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="AI Job Applier Backend",
    version="1.0",
    description="Backend API for job automation"
)

app.include_router(router)
