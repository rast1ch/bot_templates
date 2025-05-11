import os

from pydantic import BaseModel

from enums import ApplicationModeEnum


class Settings(BaseModel):
    MODE: ApplicationModeEnum = ApplicationModeEnum.DEV
    # POSTGRES_URL: str = "sqlite:///./test.db"
    # POSTGRES_USER: str = "user"
    # POSTGRES_PASSWORD: str
    # POSTGRES_DB: str = "db"
    BOT_TOKEN: str
    DB_ECHO: bool = True

    CORS_ORIGINS: list[str] = ["*"]

    LOG_LEVEL: str = "INFO"

    def __init__(self, **data) -> None:
        super().__init__(**data)

    @classmethod
    def from_env(cls) -> "Settings":
        """
        Create a Settings instance from environment variables.
        """
        _data = {
            field: os.getenv(field)
            for field in cls.__pydantic_fields__
            if os.getenv(field) is not None
        }

        return cls.model_validate(_data)


settings = Settings.from_env()
