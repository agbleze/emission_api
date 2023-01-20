FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV APP_MODULE main:app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./ .






