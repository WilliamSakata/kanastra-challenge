from fastapi import UploadFile, File
from concurrent.futures import ProcessPoolExecutor
from api.src.dtos import payers, debts
from api.src.repository import payer as payers_repository
from api.src.repository import debt as debts_repository
import csv
import codecs
        
def execute(file: UploadFile = File(...)):
    csv_reader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))

    rows = list(csv_reader)
    batch_size = 10000

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_batch, rows[i:i + batch_size]) for i in range(0, len(rows), batch_size)]
        for future in futures:
            future.result() 

def process_batch(rows):
    for row in rows:
        process_row(row)

def process_row(row):
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from api.database import Base, URL_DATABASE

    engine = create_engine(URL_DATABASE, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    payer = payers.PayerBase.from_row(row)
    debt = debts.DebtBase.from_row(row)

    db_payer = payers_repository.get_payer(db=db, payer_id=payer.id)

    if not db_payer:
        payers_repository.create_payer(db=db, payer=payer)
    
    db_debt = debts_repository.get_debt(db=db, debt_id=debt.id)

    if not db_debt:
        debts_repository.create_debt(db=db, debt=debt)
        
    db.close()