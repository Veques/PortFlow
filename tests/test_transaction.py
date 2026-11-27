import pytest
from decimal import Decimal
from datetime import date

from PortFlow.models.transaction import Transaction
from PortFlow.models.enums import TransactionType


# Valid transaction
def test_create_transaction():
    transaction = Transaction(
        asset_id=1,
        transaction_type=TransactionType.BUY,
        quantity=Decimal("10"),
        price=Decimal("150.50"),
        date=date(2026, 11, 27),
        fee=Decimal("2.50")
    )

    assert transaction.asset_id == 1
    assert transaction.transaction_type == TransactionType.BUY
    assert transaction.quantity == Decimal("10")
    assert transaction.price == Decimal("150.50")
    assert transaction.date == date(2026, 11, 27)
    assert transaction.fee == Decimal("2.50")


# Default fee
def test_default_fee():
    transaction = Transaction(
        asset_id=1,
        transaction_type=TransactionType.BUY,
        quantity=Decimal("5"),
        price=Decimal("100"),
        date=date(2026, 11, 27)
    )

    assert transaction.fee == Decimal("0")


# Invalid quantity type
def test_invalid_quantity_type():
    with pytest.raises(TypeError):
        Transaction(
            asset_id=1,
            transaction_type=TransactionType.BUY,
            quantity=10,
            price=Decimal("100"),
            date=date(2026, 11, 27)
        )


# Invalid price type
def test_invalid_price_type():
    with pytest.raises(TypeError):
        Transaction(
            asset_id=1,
            transaction_type=TransactionType.BUY,
            quantity=Decimal("10"),
            price=100,
            date=date(2026, 11, 27)
        )


# Invalid fee type
def test_invalid_fee_type():
    with pytest.raises(TypeError):
        Transaction(
            asset_id=1,
            transaction_type=TransactionType.BUY,
            quantity=Decimal("10"),
            price=Decimal("100"),
            date=date(2026, 11, 27),
            fee=2
        )


# Negative quantity
def test_negative_quantity():
    with pytest.raises(ValueError):
        Transaction(
            asset_id=1,
            transaction_type=TransactionType.BUY,
            quantity=Decimal("-10"),
            price=Decimal("100"),
            date=date(2026, 11, 27)
        )


# Negative price
def test_negative_price():
    with pytest.raises(ValueError):
        Transaction(
            asset_id=1,
            transaction_type=TransactionType.BUY,
            quantity=Decimal("10"),
            price=Decimal("-100"),
            date=date(2026, 11, 27)
        )


# Negative fee
def test_negative_fee():
    with pytest.raises(ValueError):
        Transaction(
            asset_id=1,
            transaction_type=TransactionType.BUY,
            quantity=Decimal("10"),
            price=Decimal("100"),
            date=date(2026, 11, 27),
            fee=Decimal("-2")
        )