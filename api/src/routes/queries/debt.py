from fastapi import APIRouter, Depends
from api.src.dtos import debts as schema
from api.database import get_db
from sqlalchemy.orm import Session
from api.src.repository import debt as repository

router = APIRouter()

@router.get("/debts/", response_model=list[schema.Debt])
def get_debts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return repository.get_all_debts(db=db, skip=skip, limit=limit)