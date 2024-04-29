from dotenv import dotenv_values
from nestipy.common import Module

from app_controller import AppController
from app_service import AppService
from nestipy_config import ConfigModule, ConfigOption
from src.user.user_module import UserModule


def load() -> dict:
    return dotenv_values('.env.local')


@Module(
    imports=[
        ConfigModule.for_root(ConfigOption(load=[load], ignore_env_file=True), {'is_global': True}),
        UserModule
    ],
    controllers=[AppController],
    providers=[AppService]
)
class AppModule:
    ...
