from pydantic import BaseModel
from api.src.dtos.payers import PayerBase

class DebtBase(BaseModel):
    id: str
    amount: float
    due_date: str
    payer: PayerBase

    def from_row(row):
        return DebtBase(id=row['debtId'], amount=row['debtAmount'], due_date=row['debtDueDate'], payer=PayerBase.from_row(row))

class DebtCreate(DebtBase):
    pass

class Debt(DebtBase):
    class Config:
        from_attributes = True