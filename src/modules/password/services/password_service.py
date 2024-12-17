from sqlalchemy.orm import Session
from ..models.entities.password_entity import Password

class PasswordService():
    def __init__(self):
        pass

    def create(self):
        new_password = Password();
        print(new_password)
