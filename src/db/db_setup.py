from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.settings import settings

engine = create_engine(
    settings.connection_string,
    future=True
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
    future=True,
)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()

