from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(env_file=".env")
    bot_token: str = "bot_token"
    gpt_token: str = "gpt_token"


settings = Config()
