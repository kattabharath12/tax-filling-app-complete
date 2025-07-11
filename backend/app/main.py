import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_auth, routes_profile, routes_filing, routes_upload, routes_payment, routes_submission, routes_admin

app = FastAPI(
    title="Tax Filing App",
    description="Single person tax filing for federal and state, with document upload and payment integration.",
    version="1.0.0"
)

# Configure CORS
allowed_origins = [
    "https://your-frontend-domain.com",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins if os.getenv("RAILWAY_ENVIRONMENT") else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes_auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(routes_profile.router, prefix="/api/profile", tags=["profile"])
app.include_router(routes_filing.router, prefix="/api/filing", tags=["filing"])
app.include_router(routes_upload.router, prefix="/api/upload", tags=["upload"])
app.include_router(routes_payment.router, prefix="/api/payment", tags=["payment"])
app.include_router(routes_submission.router, prefix="/api/submission", tags=["submission"])
app.include_router(routes_admin.router, prefix="/api/admin", tags=["admin"])

@app.get("/")
def read_root():
    return {"message": "Tax Filing App API", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Create tables on startup
@app.on_event("startup")
async def startup_event():
    from app.models import Base
    from app.database import engine
    Base.metadata.create_all(bind=engine)