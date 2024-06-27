from fastapi import APIRouter, UploadFile, File
from fastapi_utils.tasks import repeat_every
from api.database import get_db
from api.src.use_cases import create_debt

router = APIRouter()

@router.post("/debts/")
async def create_file(file: UploadFile = File(...)):
    create_debt.execute(file)

    return {"status": "ok"}

@router.on_event("startup")
@repeat_every(seconds=10)
def sample_cron():
    print("Running cron job")