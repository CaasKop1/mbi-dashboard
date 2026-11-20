from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_dashboard():
    return {"message": "Welcome to the MBI dashboard API"}