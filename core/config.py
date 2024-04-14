from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    main_db_user: str = "postgres"
    main_db_password: str = "p0stgresql!"
    main_db_host: str = "localhost"
    main_db_name: str = "budget-king"
    main_db_url: str = (
        f"postgresql+asyncpg://{main_db_user}:{main_db_password}@{main_db_host}/{main_db_name}"
    )

    api_v1_prefix: str = "/api/v1"


settings = Settings()
