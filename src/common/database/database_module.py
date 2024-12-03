from injector import Binder, Module, singleton
from .strategies import DatabaseStrategy, PgStrategy

class DatabaseModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(DatabaseStrategy, to=PgStrategy, scope=singleton)
