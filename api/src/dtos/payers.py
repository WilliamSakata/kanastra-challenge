from pydantic import BaseModel

class PayerBase(BaseModel):
    id: int
    name: str
    email: str

    def from_row(row): 
        return PayerBase(id=row['governmentId'], name=row['name'], email=row['email'])

class PayerCreate(PayerBase):
    pass

class Payer(PayerBase):
    class Config:
        from_attributes = True