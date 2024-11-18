FROM python:3.12.5

WORKDIR /var/www/FastAPI

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./APP/ .

CMD uvicorn main:app --host 0.0.0.0 --port 4001 --workers 4