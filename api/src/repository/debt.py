from sqlalchemy.orm import Session
from api.src.entities import debt as entity
from api.src.dtos import debts as schema
from api.database import engine
import uuid

entity.Base.metadata.create_all(bind=engine)

def get_all_debts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(entity.Debt).offset(skip).limit(limit).all()

def get_debt(db: Session, debt_id: str):
    return db.query(entity.Debt).filter(entity.Debt.id == debt_id).first()

def get_not_send_debt(db: Session, skip: int = 0, limit: int = 100):
    return db.query(entity.Debt).filter(entity.Debt.send == False).offset(skip).limit(limit).all()

def send_debt(db: Session, debt_id: str):
    db_debt = db.query(entity.Debt).filter(entity.Debt.id == debt_id).first()
    db_debt.send = True
    db.commit()
    db.refresh(db_debt)
    return db_debt

def create_debt(db: Session, debt: schema.DebtCreate):
    db_debt = entity.Debt(id=uuid.UUID(debt.id), amount=debt.amount, due_date=debt.due_date, payer_id=debt.payer.id)
    db.add(db_debt)
    db.commit()
    db.refresh(db_debt)
    return db_debt