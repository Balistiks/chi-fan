from dataclasses import dataclass
from os import getenv


@dataclass
class BotConfig:
    """Bot configuration"""

    token: str = getenv("BOT_TOKEN")
    secret_token: str = getenv("SECRET_TOKEN")


@dataclass
class Configuration:
    bot = BotConfig()


conf = Configuration()
