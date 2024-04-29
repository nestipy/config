from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy_ioc import Inject, Body, Params

from nestipy_config import ConfigService
from .user_dto import CreateUserDto, UpdateUserDto
from .user_service import UserService


@Controller('users')
class UserController:
    user_service: Inject[UserService]
    config: Inject[ConfigService]

    @Get()
    async def list(self) -> str:
        return await self.user_service.list()

    @Post()
    async def create(self, data: Body[CreateUserDto]) -> str:
        return await self.user_service.create(data)

    @Put('/{user_id}')
    async def update(self, user_id: Params[int], data: Body[UpdateUserDto]) -> str:
        return await self.user_service.update(user_id, data)

    @Delete('/{user_id}')
    async def delete(self, user_id: Params[int]) -> None:
        return await self.user_service.delete(user_id)
