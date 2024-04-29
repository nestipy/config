from nestipy.common import Injectable
from nestipy_config import ConfigService
from nestipy_ioc import Inject


@Injectable()
class AppService:
    config: Inject[ConfigService]

    @classmethod
    async def get(cls):
        return "test"

    @classmethod
    async def post(cls, data: str):
        return "test"

    @classmethod
    async def put(cls, id_: int, data: str):
        return "test"

    @classmethod
    async def delete(cls, id_: int):
        return "test"
