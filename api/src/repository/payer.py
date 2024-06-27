from sqlalchemy.orm import Session
from api.src.entities import payer as entity
from api.src.dtos import payers as schema
from api.database import engine

entity.Base.metadata.create_all(bind=engine)

def get_payer(db: Session, payer_id: int):
    return db.query(entity.Payer).filter(entity.Payer.id == payer_id).first()

def create_payer(db: Session, payer: schema.PayerCreate):
    db_payer = entity.Payer(id=payer.id, name=payer.name, email=payer.email)
    db.add(db_payer)
    db.commit()
    db.refresh(db_payer)
    return db_payer

def get_all_payers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(entity.Payer).offset(skip).limit(limit).all()