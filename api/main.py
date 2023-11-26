from fastapi import FastAPI
from routers.main_system import router as application_router  # Import the router
from authentication.endpoints import router as authentication_router
app = FastAPI()

# Include the router in your FastAPI application
app.include_router(application_router)

# Add more routers as needed
