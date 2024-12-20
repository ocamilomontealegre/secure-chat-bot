from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models.entities.base_entity import Base
from .database_strategy import DatabaseStrategy

class SqliteStrategy(DatabaseStrategy):
    def __init__(self):
        self.__engine = self.create_engine()

    def get_connection_url(self):
        return f"sqlite:///test.db"

    def create_engine(self):
        return create_engine(self.get_connection_url())

    def create_session(self):
        Session = sessionmaker(autoflush=False, bind=self.__engine)
        return Session()

    def create_tables(self):
        Base.metadata.create_all(self.__engine)
