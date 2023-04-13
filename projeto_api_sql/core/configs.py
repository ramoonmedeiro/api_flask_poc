from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):

    """
    Configurações gerais usadas na aplicação
    """

    API_PATH = '/api/v1'
    URL_DB = 'postgresql+asyncpg:/ramon:exemplo@localhost:5432/db_api'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()