import uvicorn
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scripts.service.spatial_data_service import spatial_data_obj
from scripts.postgres_db.init_db import initialize_db  # Import initialize_db

# Initialize FastAPI App
app = FastAPI()

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CORS Middleware for frontend interactions
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

# Include API Routes
app.include_router(spatial_data_obj)

# Initialize Database on Startup
@app.on_event("startup")
def startup_event():
    logger.info("Initializing Database...")
    initialize_db()  # This will create tables if they don’t exist

# Log Server Start
logger.info("FastAPI Spatial Data Server is starting...")

# Run the Server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
