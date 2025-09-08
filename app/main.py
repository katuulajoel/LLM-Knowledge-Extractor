from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import get_settings

# Initialize FastAPI app
app = FastAPI(
    title=get_settings().app_name,
    version=get_settings().app_version,
    description="LLM Knowledge Extractor - Extract and analyze knowledge from text using LLMs",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": get_settings().app_name,
        "version": get_settings().app_version
    }

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": f"Welcome to {get_settings().app_name}!",
        "version": get_settings().app_version,
        "docs": "/docs"
    }
