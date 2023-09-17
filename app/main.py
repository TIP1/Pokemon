from fastapi import FastAPI

from app.routers import api_router
from app.db_filler import download_pokemons


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    app.include_router(api_router)
    await download_pokemons()