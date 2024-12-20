import random
import string
from uuid import UUID
import zxcvbn
from injector import inject
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from common.database.strategies.database_strategy import DatabaseStrategy
from ..models.entities.password_entity import Password

class PasswordService():
    @inject
    def __init__(self, db: DatabaseStrategy):
        self.__session: Session  = db.create_session()
        self.__chars: str = string.ascii_letters + string.digits + string.punctuation

    def __check_password(self, password: str):
        result = zxcvbn.zxcvbn(password)
        feedback = result.get("feedback", {})
        score = result.get("score", 0)
        if score < 3:
            raise ValueError("Password is too weak. Consider using a stronger password.")

    def __generate_password(self, length: int) -> str:
        password = "".join(random.choices(self.__chars, k=length))
        self.__check_password(password)
        return password

    def create(self):
        new_password = Password(password=self.__generate_password(12))
        self.__session.add(new_password)
        self.__session.commit()
        return new_password

    def get(self):
        return self.__session.query(Password).all()

    def get_by_id(self, id: UUID):
        password = self.__session.get(Password, str(id))
        if not password:
            raise HTTPException(status_code=404, detail="Password not found")
        return password

    def delete_by_id(self, id: UUID):
        password = self.__session.get(Password, str(id))

        if not password:
            raise HTTPException(status_code=404, detail="Password not found")

        self.__session.delete(password)
        self.__session.commit()
        return password

