from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = 'localhost'
    port: str = 8000
    connection_string: str


settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8'
)
