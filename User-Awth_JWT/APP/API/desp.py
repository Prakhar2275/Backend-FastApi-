from APP.DB.database import sessionmaker,SessionLocal

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    