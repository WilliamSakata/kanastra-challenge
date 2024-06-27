
from sqlalchemy import Boolean, DECIMAL, Column, ForeignKey, Integer, String
from api.database import Base
from sqlalchemy.orm import relationship

class Debt(Base):
    __tablename__ = 'debts'

    id = Column(String(36), primary_key=True)
    amount = Column(DECIMAL(10, 2))
    due_date = Column(String(10))
    payer_id = Column(Integer, ForeignKey('payers.id'))
    send = Column(Boolean, default=False)

    payer = relationship('Payer', back_populates='debt')
