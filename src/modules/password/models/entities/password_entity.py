from uuid import uuid4
from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import func
from common.database.models.entities.base_entity import Base

class Password(Base):
    __tablename__ = "passwords"

    id = Column(String(36), primary_key=True, default=uuid4())
    password = Column(String, unique=False, nullable=False)
    created_at= Column(DateTime, default=func.now())
    updated_at= Column(DateTime, default=func.now(), onupdate=func.now())

