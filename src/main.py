from fastapi import FastAPI

from .routers import cameras, scanner

app = FastAPI()

app.include_router(cameras.router)
app.include_router(scanner.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
