# Pokemon

## Description

### Tech stack

1. [FastAPI](https://fastapi.tiangolo.com/)
2. [Pydantic](https://pydantic.dev/)
3. [MongoDB](https://www.mongodb.com/)

## Usage

Launch on localhost.

## Develop

Setup venv.

```console
python3.10 -m venv .venv
```

Update requirements.

```console
source ./.venv/bin/activate
pip install -r requirements.in
pip freeze > requirements.txt
```

Launch.

```console
uvicorn app.main:app 
```
