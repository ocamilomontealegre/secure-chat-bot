from typing import List
from uuid import UUID
from fastapi import APIRouter
from injector import inject
from ..services.password_service import PasswordService
from ..models.schemas.password_schema import PasswordSchema

class PasswordController:
    @inject
    def __init__(self, password_service: PasswordService):
        self.__password_service = password_service
        self.__router = APIRouter()
        self.__register_routes()

    def __register_routes(self):
        @self.__router.post(
            "",
            response_model=PasswordSchema,
            tags=["Password"],
            summary="Create a password",
            description="Create a password",
        )
        async def create():
            result = self.__password_service.create()
            return result

        @self.__router.get(
            "",
            response_model=List[PasswordSchema],
            tags=["Password"],
            summary="Get all password records",
            description="Get all password records",
        )
        async def getById():
            return self.__password_service.get()

        @self.__router.get(
            "/{id}",
            response_model=PasswordSchema,
            tags=["Password"],
            summary="Get a password by it's id",
            description="Get a password by it's id",
        )
        async def getById(id: UUID):
            return self.__password_service.get_by_id(id)

        @self.__router.delete(
            "/{id}",
            response_model=PasswordSchema,
            tags=["Password"],
            summary="Delete a password by it's id",
            description="Delete a password by it's id",
        )
        async def deleteById(id: UUID):
            return self.__password_service.delete_by_id(id)

    def get_router(self) -> APIRouter:
        return self.__router
