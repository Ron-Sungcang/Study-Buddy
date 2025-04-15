import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#Pydantic model for request body
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None

#Dummy endpoints
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)