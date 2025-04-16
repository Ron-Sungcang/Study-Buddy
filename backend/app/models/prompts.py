from pydantic import BaseModel, Field
from datetime import datetime

#Pydantic model for user prompt
class UserPrompt(BaseModel):
    name: str = None
    message: str
    subject: str
    date: datetime = Field(default_factory=datetime.astimezone)
