from fastapi import FastAPI

from .routers import cameras, motors, scanner

app = FastAPI()

app.include_router(cameras.router)
app.include_router(motors.router)
app.include_router(scanner.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/reload_config")
async def reload_config():
    ...
