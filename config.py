import os
from typing import Union

from pydantic import BaseSettings, Field


class Base(BaseSettings):
    secret_key: str = Field('random_string', env='ANOTHER_SECRET_KEY')
    port: int = 5050
    username: str = "ANAND"

    class Config:
        case_sensitive = False
        env_file = '.env'


class Dev(Base):
    username = "TRIPATHI"

    class Config:
        env_file = 'dev.env'


class Prod(Base):
    username = "Production"
    port = 5051

    class Config:
        env_file = 'prod.env'


config = dict(
    dev=Dev,
    prod=Prod
)
settings: Union[Dev, Prod] = config[os.environ.get('ENV', 'dev').lower()]()
