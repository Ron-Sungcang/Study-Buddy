from fastapi import APIRouter
from app.models.prompts import UserPrompt

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/messages")
async def create_item(prompt: UserPrompt):
    return {
        "name": prompt.name,
        "message": prompt.message,
        "subject": prompt.subject,
        "date": prompt.date.isoformat()  
        }
