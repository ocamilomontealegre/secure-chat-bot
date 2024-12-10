from injector import Binder, Module, singleton
from common.env import get_env_variables
from .strategies import DatabaseStrategy, PgStrategy


class DatabaseModule(Module):
    def __init__(self):
        self.__env = get_env_variables().pg

    def configure(self, binder: Binder) -> None:
        binder.bind(DatabaseStrategy, to=lambda: PgStrategy(
            pg_env=self.__env), scope=singleton)
