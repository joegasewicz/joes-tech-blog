from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker


def init_db() -> Engine:
    pg_url = f"postgresql://admin:admin@localhost:5432/blog_db"
    engine = create_engine(pg_url, echo=True)
    return engine


def create_session() -> Session:
    engine = init_db()
    _Session = sessionmaker(bind=engine)
    session = _Session()
    return session
