# TRAMIL-API

Structured database and REST API for TRAMIL Caribbean medicinal plants

**Contributing to ethnopharmacological research through open data and programmatic access.**

## 🎯 Project Overview

TRAMIL-API is a comprehensive, machine-readable database derived from [TRAMIL (Program of Applied Research to Popular Medicine in the Caribbean)](https://tramil.net). This project structures traditional Caribbean medicinal plant knowledge into a normalized database and exposes it via a REST API for researchers, health professionals, educators, and students.

### Key Features
- **Complete plant monographs** from TRAMIL library (scientific names, botanical families, vernacular names)
- **Traditional uses & preparations** (remedies, routes of administration, health indications)
- **Media assets** (botanical illustrations, herbarium specimens, photographs)
- **Safety & toxicity information** (warnings, contraindications, evidence levels)
- **Research metadata** (geographic regions, preparation methods, historical references)
- **REST API** with OpenAPI/Swagger documentation
- **Machine-readable formats** (JSON, CSV) for statistical analysis and meta-analyses

## 📊 Data Model

### Core Entities
```
Plants
├── id (UUID)
├── scientific_name
├── author_abbreviation
├── botanical_family_id
├── vernacular_names[] (multilingual)
├── geographic_distribution[]
├── uses[] (with evidence levels)
├── preparations[]
├── toxicity_info
└── media[] (images, herbarium, drawings)

Families
├── id
├── name (botanical family)
└── plant_count

HealthProblems
├── id
├── name (health indication)
├── category (ICD-10 reference)
└── associated_plants[]

Uses
├── plant_id
├── health_problem_id
├── preparation_type
├── route_of_administration
├── evidence_level
└── safety_notes
```

## 🔧 Tech Stack

- **Data Collection**: n8n (workflow automation)
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL / SQLite
- **Data Storage**: GitHub (JSON/CSV for version control)
- **API Documentation**: OpenAPI 3.0 / Swagger UI
- **Deployment**: Railway / Render (planned)
- **Version Control**: Git

## 🚀 Quickstart

### Installation
```bash
git clone https://github.com/GuillaumeBld/tramil-api.git
cd tramil-api

# Create Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the API
```bash
# From project root
uvicorn app.main:app --reload

# API will be available at http://localhost:8000
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

### Data Update Workflow (n8n)
1. n8n workflow crawls TRAMIL A-Z plant index
2. Extracts plant URLs and metadata
3. Parses each plant monograph HTML
4. Normalizes data according to schema
5. Commits JSON/CSV to GitHub
6. Triggers API reindex

## 📚 API Endpoints (MVP)

### Plants
- `GET /plants` - List all plants (paginated)
- `GET /plants/{id}` - Get plant details with uses and media
- `GET /plants?family={family}` - Filter by botanical family
- `GET /plants?health_problem={id}` - Find plants used for specific health problem
- `GET /plants/search?q={query}` - Full-text search

### Families
- `GET /families` - List all botanical families
- `GET /families/{id}/plants` - Get plants in family

### Health Problems
- `GET /health-problems` - List health indications
- `GET /health-problems/{id}/plants` - Find plants for indication

### Media
- `GET /plants/{id}/media` - Get all media for plant

## 🔐 Attribution & Legal

This project respects TRAMIL's intellectual property and scientific work:
- **Data source**: [TRAMIL Network](https://tramil.net) - Contributors from Caribbean universities and research institutions
- **License**: MIT (code) + Proper attribution to TRAMIL in API responses
- **Use restrictions**: Non-commercial research and education (to be confirmed with TRAMIL)
- **Citation format**: All API responses include `source: TRAMIL`, `source_url`, and `date_accessed`

## 📋 Project Roadmap

### Phase 1 (MVP - In Progress)
- [ ] Define data schema and n8n crawler workflow
- [ ] Scrape and normalize 200+ TRAMIL plants
- [ ] Build FastAPI with core endpoints
- [ ] Generate OpenAPI documentation
- [ ] Deploy API to Railway
- [ ] Contact TRAMIL for collaboration

### Phase 2 (Expansion)
- [ ] Complete monograph coverage (all ~600 plants)
- [ ] Add publication/research references
- [ ] Implement advanced filtering (preparation type, geographic region)
- [ ] Add multilingual support (FR/ES/EN)
- [ ] Create web UI for data exploration

### Phase 3 (Integration)
- [ ] GraphQL API variant
- [ ] Data export formats (CSV, RDF, LD-JSON)
- [ ] Integration with herbarium collections
- [ ] Machine learning: plant similarity recommendations

## 🤝 Contributing

This project aims to **contribute to ethnopharmacological research** while respecting TRAMIL's work.

Before contributing:
1. Understand TRAMIL's mission and legal requirements
2. Ensure all contributions properly attribute TRAMIL
3. Follow the data schema in `docs/schema.json`
4. Test changes against `tests/`

## 📧 Contact & Collaboration

To propose collaboration with TRAMIL or discuss this project:
- GitHub Issues: [Project discussions](https://github.com/GuillaumeBld/tramil-api/issues)
- TRAMIL Contact: https://tramil.net/en/contact

## 📖 Documentation

- `docs/schema.json` - Complete data schema
- `docs/n8n-workflow.md` - n8n crawler configuration
- `docs/api-examples.md` - API usage examples
- `CONTRIBUTING.md` - Contribution guidelines

## ⚖️ License

Code: MIT License  
Data attribution: TRAMIL Network (all responses include source attribution)

---

**Status**: MVP Development in Progress  
**Last Updated**: January 2026  
**Contact**: @GuillaumeBld
