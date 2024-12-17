from fastapi import APIRouter
from injector import Injector
from health.controllers.health_controller import HealthController
from modules.password.controllers.password_controller import PasswordController
from app.enums.app_endpoints_enum import AppEndpoints


class AppRouter:
    def __init__(self, injector: Injector):
        self.__router = APIRouter()
        self.__injector = injector
        self.__register_routes()

    def __register_routes(self):
        health_controller = self.__injector.get(HealthController)
        password_controller = self.__injector.get(PasswordController)

        self.__router.include_router(
            health_controller.get_router(),
            prefix=f"{AppEndpoints.HEALTH.value}",
        )

        self.__router.include_router(
            password_controller.get_router(),
            prefix=f"{AppEndpoints.PASSWORD.value}"
        )

    def get_router(self) -> APIRouter:
        return self.__router
