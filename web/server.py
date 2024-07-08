from contextlib import asynccontextmanager
from pathlib import Path

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from uvicorn import run
from fastapi import FastAPI, HTTPException

from web.routers import trips, users, cars


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")


__static_files_path = Path(__file__).parent / "front" / "static"
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root() -> FileResponse:
    return FileResponse(__static_files_path / "index.html")


app.mount("/static", StaticFiles(directory=__static_files_path), name="static")


def start():
    app.include_router(trips.router)
    app.include_router(users.router)
    app.include_router(cars.router)
    run(app, port=5500)
