from injector import Binder, Module
from health.health_module import HealthModule
from common.database.database_module import DatabaseModule
from modules.password.password_module import PasswordModule


class AppModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.install(HealthModule())
        binder.install(DatabaseModule())
        binder.install(PasswordModule())
