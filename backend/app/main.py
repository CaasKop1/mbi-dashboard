from fastapi import FastAPI
from app.api import dashboard

app = FastAPI(
    title="MBI API",
    description="Backend API for the MBI dashboard",
    version="1.0.0"
)

app.include_router(
    dashboard.router,
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}

