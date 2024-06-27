import os
from pathlib import Path
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from api.database import Base, get_db
from api.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

def test_create():
    test_upload_file = Path('./', 'input-test.csv')
    file_path = os.path.join(__location__, test_upload_file)
    
    files = {'file': ('input-test.csv', open(file_path, 'rb'))}

    test_file = open(os.path.join(__location__, test_upload_file), 'rb')

    file_payload = {'upload_file': test_file}

    response = client.post("/debts", files=files)

    test_file.close()
    assert response.status_code == 200
