from fastapi import FastAPI
from api.src.routes.commands import debt as debt_command
from api.src.routes.queries import debt as debt_query
from api.src.use_cases import send_debt
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://localhost",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def cron_job():
    send_debt.execute()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.start()
    
    scheduler.add_job(
        cron_job,
        trigger=IntervalTrigger(seconds=60),
        id="cron_job",
        name="Envia débitos pendentes a cada 1 minuto",
        replace_existing=True,
    )
    logger.info("Scheduler inicializado.")

@app.on_event("startup")
async def startup():
    start_scheduler()

app.include_router(debt_command.router)
app.include_router(debt_query.router)