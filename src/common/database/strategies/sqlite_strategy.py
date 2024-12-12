from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .database_strategy import DatabaseStrategy

class SqliteStrategy(DatabaseStrategy):
    def get_connection_url(self):
        return f"sqlite:///test.db"

    def create_engine(self):
        return create_engine(self.get_connection_url())

    def create_session(self):
        engine = self.create_engine()
        Session = sessionmaker(bind=engine)
        return Session()
