from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the API router
from api.router import api_router
from core.config import settings

# Create FastAPI instance
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router with prefix
app.include_router(api_router, prefix=settings.API_PREFIX)

# Health check endpoint
@app.get("/healthcheck")
async def health_check():
    """Checks if server is active. Thank you"""
    return {"status": "active"}

# Main entry point for running the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
