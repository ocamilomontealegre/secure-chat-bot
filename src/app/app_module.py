from injector import Binder, Module
from common.database.database_module import DatabaseModule
from health.health_module import HealthModule


class AppModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.install(HealthModule())
        binder.install(DatabaseModule())
