"""
Payment service using Stripe API.
"""

import stripe
from decimal import Decimal
from typing import Optional, Dict
from datetime import datetime


class PaymentService:
    """
    Service to handle payment operations via Stripe.
    """

    def __init__(self, api_key: str):
        """Initialize payment service with Stripe API key."""
        stripe.api_key = api_key
        self.currency = "eur"

    def create_payment(
        self,
        amount: Decimal,
        customer_email: str,
        description: Optional[str] = None
    ) -> Dict:
        """
        Create a payment intent.

        Args:
            amount: Amount in euros (will be converted to cents)
            customer_email: Customer email address
            description: Optional payment description

        Returns:
            Dict with payment details

        Raises:
            ValueError: If amount is invalid
            stripe.error.StripeError: If Stripe API fails
        """
        # Validate amount
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > Decimal("999999.99"):
            raise ValueError("Amount exceeds maximum allowed")

        # Convert to cents
        amount_cents = int(amount * 100)

        # Create payment intent
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount_cents,
                currency=self.currency,
                receipt_email=customer_email,
                description=description or "Payment",
            )

            return {
                "payment_id": intent.id,
                "amount": amount,
                "currency": self.currency,
                "status": intent.status,
                "customer_email": customer_email,
                "created_at": datetime.fromtimestamp(intent.created),
            }

        except stripe.error.CardError as e:
            raise ValueError(f"Card error: {e.user_message}")

        except stripe.error.StripeError as e:
            raise RuntimeError(f"Stripe API error: {str(e)}")

    def confirm_payment(self, payment_id: str) -> bool:
        """
        Confirm a payment intent.

        Args:
            payment_id: Stripe payment intent ID

        Returns:
            True if payment confirmed successfully

        Raises:
            ValueError: If payment_id is invalid
            RuntimeError: If confirmation fails
        """
        if not payment_id or not payment_id.startswith("pi_"):
            raise ValueError("Invalid payment ID")

        try:
            intent = stripe.PaymentIntent.confirm(payment_id)
            return intent.status == "succeeded"

        except stripe.error.StripeError as e:
            raise RuntimeError(f"Payment confirmation failed: {str(e)}")

    def refund_payment(
        self,
        payment_id: str,
        amount: Optional[Decimal] = None
    ) -> Dict:
        """
        Refund a payment (full or partial).

        Args:
            payment_id: Stripe payment intent ID
            amount: Amount to refund (None = full refund)

        Returns:
            Dict with refund details

        Raises:
            ValueError: If parameters are invalid
            RuntimeError: If refund fails
        """
        if not payment_id or not payment_id.startswith("pi_"):
            raise ValueError("Invalid payment ID")

        try:
            params = {"payment_intent": payment_id}

            if amount is not None:
                if amount <= 0:
                    raise ValueError("Refund amount must be positive")
                params["amount"] = int(amount * 100)

            refund = stripe.Refund.create(**params)

            return {
                "refund_id": refund.id,
                "payment_id": payment_id,
                "amount": Decimal(refund.amount) / 100,
                "status": refund.status,
                "created_at": datetime.fromtimestamp(refund.created),
            }

        except stripe.error.StripeError as e:
            raise RuntimeError(f"Refund failed: {str(e)}")

    def get_payment_status(self, payment_id: str) -> str:
        """
        Get current status of a payment.

        Args:
            payment_id: Stripe payment intent ID

        Returns:
            Payment status string

        Raises:
            ValueError: If payment_id is invalid
            RuntimeError: If status retrieval fails
        """
        if not payment_id or not payment_id.startswith("pi_"):
            raise ValueError("Invalid payment ID")

        try:
            intent = stripe.PaymentIntent.retrieve(payment_id)
            return intent.status

        except stripe.error.StripeError as e:
            raise RuntimeError(f"Failed to retrieve status: {str(e)}")
