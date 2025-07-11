from fastapi import APIRouter, HTTPException
import stripe
import os

router = APIRouter()

# stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@router.post("/create-intent")
def create_payment_intent(amount: int):
    return {"message": "Payment intent created", "client_secret": "demo_secret"}

@router.post("/confirm")
def confirm_payment(payment_data: dict):
    return {"message": "Payment confirmed", "status": "succeeded"}