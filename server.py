from fastapi import FastAPI

from web.routers import trips, users

# Create FastAPI instance
app = FastAPI()

# Include the routers
app.include_router(trips.router)
app.include_router(users.router)


# Example endpoint to check if the server is running
@app.get("/")
async def root():
    return {"message": "Server is running"}


# Add any startup/shutdown events if necessary to manage resources
@app.on_event("startup")
async def startup_event():
    print("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")

