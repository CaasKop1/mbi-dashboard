from fastapi import FastAPI

app = FastAPI(
    title="MBI API",
    description="Backend API for the MBI dashboard",
    version="1.0.0"
)

@app.get("/")
def test():
    return {"message": "Welcome to the MBI API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

