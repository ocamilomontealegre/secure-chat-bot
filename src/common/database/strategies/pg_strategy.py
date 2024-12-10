from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .database_strategy import DatabaseStrategy
from common.env.pg_env_config import PgEnvVariables


class PgStrategy(DatabaseStrategy):
    def __init__(self, pg_env: PgEnvVariables):
        self.host = pg_env.host
        self.port = pg_env.port
        self.username = pg_env.username
        self.password = pg_env.password
        self.database = pg_env.database

    def get_connection_url(self):
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

    def create_engine(self):
        return create_engine(self.get_connection_url())

    def create_session(self):
        engine = self.create_engine()
        Session = sessionmaker(bind=engine)
        return Session()
