# Configurable forms and tax rules
SUPPORTED_FORMS = [
    {
        "name": "1040",
        "title": "Form 1040 - U.S. Individual Income Tax Return",
        "fields": [
            {"name": "first_name", "type": "text", "required": True},
            {"name": "last_name", "type": "text", "required": True},
            {"name": "ssn", "type": "ssn", "required": True},
            {"name": "filing_status", "type": "select", "options": ["single", "married_joint", "married_separate", "head_of_household"]},
            {"name": "wages", "type": "currency", "required": True},
            {"name": "interest", "type": "currency"},
            {"name": "dividends", "type": "currency"}
        ]
    },
    {
        "name": "schedule_a",
        "title": "Schedule A - Itemized Deductions",
        "fields": [
            {"name": "medical_expenses", "type": "currency"},
            {"name": "state_local_taxes", "type": "currency"},
            {"name": "mortgage_interest", "type": "currency"},
            {"name": "charitable_contributions", "type": "currency"}
        ]
    },
    {
        "name": "schedule_c",
        "title": "Schedule C - Profit or Loss From Business",
        "fields": [
            {"name": "business_name", "type": "text"},
            {"name": "business_income", "type": "currency"},
            {"name": "business_expenses", "type": "currency"}
        ]
    }
]

SUPPORTED_STATES = [
    {"code": "CA", "name": "California", "form": "540"},
    {"code": "NY", "name": "New York", "form": "IT-201"},
    {"code": "TX", "name": "Texas", "form": "residency"}
]
