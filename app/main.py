"""Main FastAPI application for TRAMIL-API."""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum

# Initialize FastAPI app
app = FastAPI(
    title="TRAMIL-API",
    description="Structured REST API for TRAMIL Caribbean medicinal plants database",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# Pydantic Models
# ============================================================================

class PreparationType(str, Enum):
    """Type de préparation."""
    INFUSION = "infusion"
    DECOCTION = "decoction"
    POULTICE = "poultice"
    TINCTURE = "tincture"
    JUICE = "juice"
    POWDER = "powder"
    TEA = "tea"
    OTHER = "other"

class RouteOfAdministration(str, Enum):
    """Voie d'administration."""
    ORAL = "oral"
    TOPICAL = "topical"
    INHALATION = "inhalation"
    OTHER = "other"

class EvidenceLevel(str, Enum):
    """Niveau de preuve."""
    TRADITIONAL = "traditional"
    SUPPORTED = "supported"
    DOCUMENTED = "documented"
    CLINICAL = "clinical"

class Use(BaseModel):
    """Health use of a plant."""
    health_problem: str
    preparation_type: PreparationType
    route_of_administration: RouteOfAdministration
    evidence_level: EvidenceLevel
    safety_notes: Optional[str] = None

class Media(BaseModel):
    """Media asset."""
    type: str = Field(..., description="Type: photo, drawing, herbarium, scan, section")
    url: str
    credit: Optional[str] = None
    caption: Optional[str] = None

class Source(BaseModel):
    """Data source information."""
    name: str = "TRAMIL"
    url: str
    date_accessed: datetime

class Plant(BaseModel):
    """Plant monograph."""
    id: str
    scientific_name: str
    author_abbreviation: Optional[str] = None
    botanical_family: str
    vernacular_names: dict = Field(default_factory=dict)
    geographic_distribution: List[str] = []
    uses: List[Use] = []
    toxicity_info: Optional[dict] = None
    media: List[Media] = []
    source: Source

class Family(BaseModel):
    """Botanical family."""
    id: str
    name: str
    plant_count: int = 0

class HealthProblem(BaseModel):
    """Health indication."""
    id: str
    name: str
    category: Optional[str] = None

# ============================================================================
# Routes
# ============================================================================

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information."""
    return {
        "name": "TRAMIL-API",
        "description": "Structured REST API for TRAMIL Caribbean medicinal plants",
        "version": "0.1.0",
        "docs": "/docs",
        "endpoints": {
            "plants": "/plants",
            "families": "/families",
            "health-problems": "/health-problems"
        },
        "source": "TRAMIL Network",
        "source_url": "https://tramil.net"
    }

@app.get("/health", tags=["Health Check"])
async def health_check():
    """Health check endpoint."""
    return {"status": "operational", "timestamp": datetime.now()}

@app.get("/plants", response_model=List[Plant], tags=["Plants"])
async def list_plants(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max records to return"),
    family: Optional[str] = Query(None, description="Filter by botanical family"),
    search: Optional[str] = Query(None, description="Full-text search")
):
    """List all plants with optional filtering."""
    # TODO: Implement database query
    return []

@app.get("/plants/{plant_id}", response_model=Plant, tags=["Plants"])
async def get_plant(plant_id: str):
    """Get a single plant by ID."""
    # TODO: Implement database query
    return JSONResponse(
        status_code=404,
        content={"detail": f"Plant {plant_id} not found"}
    )

@app.get("/plants/search", tags=["Plants"])
async def search_plants(q: str = Query(..., min_length=2)):
    """Search plants by name or properties."""
    # TODO: Implement full-text search
    return []

@app.get("/families", response_model=List[Family], tags=["Families"])
async def list_families():
    """List all botanical families."""
    # TODO: Implement database query
    return []

@app.get("/families/{family_id}/plants", tags=["Families"])
async def get_family_plants(family_id: str):
    """Get all plants in a botanical family."""
    # TODO: Implement database query
    return []

@app.get("/health-problems", response_model=List[HealthProblem], tags=["Health Problems"])
async def list_health_problems():
    """List all health indications."""
    # TODO: Implement database query
    return []

@app.get("/health-problems/{problem_id}/plants", tags=["Health Problems"])
async def get_plants_by_health_problem(problem_id: str):
    """Get plants used for a specific health problem."""
    # TODO: Implement database query
    return []

@app.get("/statistics", tags=["Statistics"])
async def get_statistics():
    """Get database statistics."""
    return {
        "total_plants": 0,
        "total_families": 0,
        "total_health_problems": 0,
        "data_version": "0.1.0",
        "last_updated": None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
