from typing import Annotated
from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy.ioc import Inject, Body, Param

from nestipy_config import ConfigService
from .user_dto import CreateUserDto, UpdateUserDto
from .user_service import UserService


@Controller('users')
class UserController:
    user_service: Annotated[UserService, Inject()]
    config: Annotated[ConfigService, Inject()]

    @Get()
    async def list(self) -> str:
        return await self.user_service.list()

    @Post()
    async def create(self, data: Annotated[CreateUserDto, Body()]) -> str:
        return await self.user_service.create(data)

    @Put('/{user_id}')
    async def update(self, user_id: Annotated[int, Param('user_id')], data: Annotated[UpdateUserDto, Body()]) -> str:
        return await self.user_service.update(user_id, data)

    @Delete('/{user_id}')
    async def delete(self, user_id: Annotated[int, Param('user_id')]) -> None:
        return await self.user_service.delete(user_id)
