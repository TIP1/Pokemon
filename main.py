from fastapi import FastAPI
import uvicorn
from routers.route import router

app = FastAPI()

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(app='main:app', port=8080, reload=True)