from fastapi import APIRouter

from .route import router as pokemon_router

api_router = APIRouter()


api_router.include_router(pokemon_router, prefix="/pokemons", tags=["pokemons"])