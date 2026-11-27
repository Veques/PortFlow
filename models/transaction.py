from dataclasses import dataclass
from decimal import Decimal
from datetime import date
from .enums import TransactionType


@dataclass
class Transaction:
    asset_id: int
    transaction_type: TransactionType
    quantity: Decimal
    price: Decimal
    date: date
    fee: Decimal = Decimal("0")
    id: int | None = None

    def __post_init__(self):
        if not isinstance(self.quantity, Decimal):
            raise TypeError("Quantity must be a decimal value")

        if not isinstance(self.price, Decimal):
            raise TypeError("Price must be a decimal value")

        if not isinstance(self.fee, Decimal):
            raise TypeError("Fee must be a decimal value")

        if self.price <= 0 or self.quantity <= 0 or self.fee < 0:
            raise ValueError(
                "Make sure you entered valid values for price, quantity and fee"
            )