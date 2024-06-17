from fastapi import FastAPI
from routers import trips, users

app = FastAPI()

app.include_router(trips.router)
app.include_router(users.router)
