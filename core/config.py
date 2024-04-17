from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):
    main_db_user: str
    main_db_password: str
    main_db_host: str
    main_db_name: str
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


class Settings(BaseSettings):
    db: DbSettings = DbSettings(
        _env_file=".env",
    )
    main_db_url: str = (
        f"postgresql+asyncpg://{db.main_db_user}:{db.main_db_password}@{db.main_db_host}/{db.main_db_name}"
    )
    api_v1_prefix: str = "/api/v1"


settings = Settings()
