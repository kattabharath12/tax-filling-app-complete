from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Get database URL from Railway
DATABASE_URL = os.getenv("DATABASE_URL")

# Railway provides postgres:// but SQLAlchemy 1.4+ requires postgresql://
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# For local development
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./tax_filing.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()