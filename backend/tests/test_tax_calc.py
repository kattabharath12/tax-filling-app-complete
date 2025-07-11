import pytest
from app.tax_calc import calculate_federal_tax, calculate_standard_deduction

def test_standard_deduction():
    # Test standard deduction calculation
    assert calculate_standard_deduction("single", 2023) == 13850
    assert calculate_standard_deduction("married_joint", 2023) == 27700

def test_federal_tax_calculation():
    # Test basic federal tax calculation
    result = calculate_federal_tax({
        "wages": 50000,
        "filing_status": "single",
        "deductions": 13850
    })
    assert result["taxable_income"] == 36150
    assert result["tax_owed"] > 0
