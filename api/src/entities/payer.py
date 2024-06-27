
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base

class Payer(Base):
    __tablename__ = 'payers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    debt = relationship('Debt', back_populates='payer')