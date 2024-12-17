from fastapi import APIRouter
from injector import inject
from ..services.password_service import PasswordService

class PasswordController:
    @inject
    def __init__(self, password_service: PasswordService):
        self.__password_service = password_service
        self.__router = APIRouter()
        self.__register_routes()

    def __register_routes(self):
        @self.__router.post(
            "",
            response_model="",
            tags=["Password"],
            summary="Create a password",
            description="Create a password",
        )
        async def create():
            return self.__password_service.create()

    def get_router(self) -> APIRouter:
        return self.__router
