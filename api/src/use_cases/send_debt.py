from api.database import SessionLocal
from api.src.repository.debt import get_not_send_debt, send_debt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def execute():
    db = SessionLocal()
    debts = get_not_send_debt(db)
    for debt in debts:
        logger.info(f"Enviando debt: {debt.id}")
        send_debt(db, debt.id)
    db.close()
    logger.info("Debts enviados com sucesso.")