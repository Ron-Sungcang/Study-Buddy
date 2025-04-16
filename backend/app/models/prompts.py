from pydantic import BaseModel, ConfigDict
from datetime import datetime, timezone

#Pydantic model for user prompt
class UserPrompt(BaseModel):
    name: str = None
    message: str
    subject: str
    date: datetime = datetime.now(timezone.utc)  # Default to current UTC time

    model_config = ConfigDict(from_attributes=True)