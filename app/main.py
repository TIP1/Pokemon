import asyncio

from fastapi import FastAPI

from app.routers import api_router
from app.db_filler import download_pokemons


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    bg_tasks = set()
    task = asyncio.create_task(download_pokemons())
    app.include_router(api_router)
    bg_tasks.add(task)
    task.add_done_callback(bg_tasks.discard)