from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "localhost"
    port: int = 8080
    connection_string: str


settings = Settings(
    #_env_file='../.env', #for migration bug
    _env_file='.env',
    _env_file_encoding='utf-8'
)
