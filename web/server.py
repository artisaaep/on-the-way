from contextlib import asynccontextmanager
from pathlib import Path

from starlette.responses import FileResponse
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


@app.get("/{static_file_location}", include_in_schema=False)
async def index(static_file_location: str) -> FileResponse:
    correct_path = __static_files_path
    for path_part in static_file_location.split('/'):
        correct_path = correct_path / path_part
    if correct_path.exists():
        return FileResponse(correct_path)

    raise HTTPException(
        status_code=404,
        detail="Page not found",
    )


def start():
    app.include_router(trips.router)
    app.include_router(users.router)
    app.include_router(cars.router)
    run(app)
