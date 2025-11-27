import uvicorn
from fastapi import FastAPI

from handlers import route

def get_app() -> FastAPI:
    application = FastAPI()
    application.include_router(route)
    return application

app = get_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
