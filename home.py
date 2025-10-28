from fastapi import APIRouter, HTTPException

home_router = APIRouter(prefix="/home", tags=["Home"])

@home_router.get("/")
async def home():
    return {"message": "hello there!"}