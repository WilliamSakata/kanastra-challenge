FROM python:3.12-slim-bookworm

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y gcc python3-dev

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]