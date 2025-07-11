import pytest
from app.ocr_mock import extract_fields_from_document

def test_w2_extraction():
    # Test W-2 data extraction
    result = extract_fields_from_document("sample_w2.pdf", "W-2")
    assert "employer" in result
    assert "wages" in result
    assert "ssn" in result

def test_1099_extraction():
    # Test 1099 data extraction
    result = extract_fields_from_document("sample_1099.pdf", "1099-NEC")
    assert "payer" in result
    assert "nonemployee_compensation" in result
