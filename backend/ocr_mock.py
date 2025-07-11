def extract_fields_from_document(file_path: str, doc_type: str):
    """Mock OCR extraction - returns sample data based on document type"""

    if doc_type == "W-2":
        return {
            "employer": "Demo Corporation",
            "employee_name": "John Doe",
            "ssn": "123-45-6789",
            "wages": 50000.00,
            "federal_tax_withheld": 7500.00,
            "state_tax_withheld": 2000.00,
            "social_security_wages": 50000.00,
            "medicare_wages": 50000.00
        }
    elif doc_type == "1099-NEC":
        return {
            "payer": "Client Company LLC",
            "recipient_name": "John Doe",
            "ssn": "123-45-6789",
            "nonemployee_compensation": 15000.00,
            "federal_tax_withheld": 0.00
        }
    elif doc_type == "1099-MISC":
        return {
            "payer": "Investment Firm",
            "recipient_name": "John Doe",
            "ssn": "123-45-6789",
            "rents": 0.00,
            "royalties": 0.00,
            "other_income": 500.00
        }
    else:
        return {"error": "Unsupported document type"}
