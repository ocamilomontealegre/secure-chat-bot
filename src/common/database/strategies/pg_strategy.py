from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .database_strategy import DatabaseStrategy

class PgStrategy(DatabaseStrategy):
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    def get_connection_url(self):
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

    def create_engine(self):
        return create_engine(self.get_connection_url())

    def create_session(self):
        engine = self.create_engine()
        Session = sessionmaker(bind=engine)
        return Session()

