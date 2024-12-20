from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class PasswordSchema(BaseModel):
    id: UUID
    password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode: True
