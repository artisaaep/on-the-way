from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    base_webapp_url: SecretStr
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / '.env',
        env_file_encoding="utf-8"
    )


config = Settings()
base_webapp_url = config.base_webapp_url.get_secret_value()
