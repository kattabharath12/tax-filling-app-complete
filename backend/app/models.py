from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String)
    ssn_encrypted = Column(String)  # Encrypted
    dob = Column(Date)
    address_encrypted = Column(String)  # Encrypted
    role = Column(String, default="user")
    created_at = Column(DateTime, default=datetime.utcnow)

    filings = relationship("Filing", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="user")

class Filing(Base):
    __tablename__ = "filings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    year = Column(Integer)
    federal_form = Column(Text)  # JSON stringified
    state_form = Column(Text)    # JSON stringified
    status = Column(String, default="in_progress")
    tax_owed = Column(Float, default=0.0)
    refund_amount = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="filings")
    documents = relationship("Document", back_populates="filing")

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filing_id = Column(Integer, ForeignKey("filings.id"))
    filename = Column(String)
    file_path = Column(String)
    doc_type = Column(String)  # W-2, 1099-NEC, etc.
    extracted_data = Column(Text)  # JSON stringified
    created_at = Column(DateTime, default=datetime.utcnow)

    filing = relationship("Filing", back_populates="documents")

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String)
    details = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="audit_logs")
