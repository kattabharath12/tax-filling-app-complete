from fastapi import APIRouter, Depends, HTTPException
from app.tax_calc import calculate_federal_tax

router = APIRouter()

@router.post("/calculate")
def calculate_tax(form_data: dict):
    result = calculate_federal_tax(form_data)
    return {"calculation": result}

@router.get("/forms")
def get_forms():
    from app.config import SUPPORTED_FORMS
    return {"forms": SUPPORTED_FORMS}

@router.post("/save")
def save_filing(filing_data: dict):
    return {"message": "Filing saved successfully", "filing_id": 1}