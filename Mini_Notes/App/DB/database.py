from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database file
DATABASE_URL = "sqlite:///./notes.db"

# connect to database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# session to talk to database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# base class for models
Base = declarative_base()


# dependency for routes later
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()