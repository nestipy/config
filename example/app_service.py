from typing import Annotated

from nestipy.common import Injectable
from nestipy_config import ConfigService
from nestipy.ioc import Inject


@Injectable()
class AppService:
    config: Annotated[ConfigService, Inject()]

    @classmethod
    async def get(cls):
        return "test"

    @classmethod
    async def post(cls, data: dict):
        return "test"

    @classmethod
    async def put(cls, id_: int, data: dict):
        return "test"

    @classmethod
    async def delete(cls, id_: int):
        return "test"
