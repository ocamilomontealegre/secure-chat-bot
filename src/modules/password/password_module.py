from injector import Binder, Module, singleton
from .controllers.password_controller import PasswordController
from .services.password_service import PasswordService


class PasswordModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(PasswordController, to=PasswordController, scope=singleton)
        binder.bind(PasswordService, to=PasswordService, scope=singleton)
