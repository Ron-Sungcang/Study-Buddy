import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

app = FastAPI()

origins = [
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#Pydantic model for user prompt
class userPrompt(BaseModel):
    name: str = None
    message: str
    subject: str
    date: datetime = Field(default_factory=datetime.timezone.utc)

#Dummy endpoints
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/app/message")
async def message(prompt: userPrompt):
    return {"message": prompt.message}

@app.post("/app/messages")
async def create_item(prompt: userPrompt):
    return {"name": prompt.name, "messahe": prompt.message}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)