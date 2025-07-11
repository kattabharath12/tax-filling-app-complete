def calculate_standard_deduction(filing_status: str, year: int = 2023):
    """Calculate standard deduction based on filing status and year"""
    deductions_2023 = {
        "single": 13850,
        "married_joint": 27700,
        "married_separate": 13850,
        "head_of_household": 20800
    }
    return deductions_2023.get(filing_status, 13850)

def calculate_federal_tax(form_data: dict):
    """Calculate federal tax owed/refund"""
    wages = form_data.get("wages", 0)
    filing_status = form_data.get("filing_status", "single")
    itemized_deductions = form_data.get("itemized_deductions", 0)

    # Standard vs itemized deduction
    standard_deduction = calculate_standard_deduction(filing_status)
    deduction = max(standard_deduction, itemized_deductions)

    # Taxable income
    taxable_income = max(0, wages - deduction)

    # Simplified tax calculation (2023 brackets for single filers)
    tax_owed = 0
    if taxable_income > 0:
        if taxable_income <= 11000:
            tax_owed = taxable_income * 0.10
        elif taxable_income <= 44725:
            tax_owed = 1100 + (taxable_income - 11000) * 0.12
        else:
            tax_owed = 5147 + (taxable_income - 44725) * 0.22

    # Withholding
    federal_withholding = form_data.get("federal_tax_withheld", 0)

    # Refund or amount owed
    if federal_withholding > tax_owed:
        refund = federal_withholding - tax_owed
        amount_owed = 0
    else:
        refund = 0
        amount_owed = tax_owed - federal_withholding

    return {
        "taxable_income": taxable_income,
        "deduction_used": deduction,
        "tax_owed": tax_owed,
        "federal_withholding": federal_withholding,
        "refund": refund,
        "amount_owed": amount_owed
    }
