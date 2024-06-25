from fastapi import FastAPI

from web.routers import trips, users, cars

app = FastAPI()

app.include_router(trips.router)
app.include_router(users.router)
app.include_router(cars.router)


@app.get("/")
async def root():
    return {"message": "Server is running"}


@app.on_event("startup")
async def startup_event():
    print("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")

