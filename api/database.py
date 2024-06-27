from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()
import os

URL_DATABASE = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    os.getenv('DATABASE_USERNAME'),
    os.getenv('DATABASE_PASSWORD'),
    os.getenv('DATABASE_HOST'),
    os.getenv('DATABASE_PORT'),
    os.getenv('DATABASE')
)

engine = create_engine(URL_DATABASE, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
