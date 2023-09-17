# Tiangolo's base image which is fine to use with compose
# https://fastapi.tiangolo.com/deployment/docker/#when-to-use
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app