from datetime import date

from app.money import dollars_to_cents
from app.services import calculate_status, remaining_balance


def test_money_conversion():
    assert dollars_to_cents("1,234.56") == 123456


def test_partial_status():
    assert calculate_status(
        estimated_cents=100000,
        paid_cents=50000,
        due_date="2026-12-31",
        as_of=date(2026, 6, 1),
    ) == "PARTIALLY PAID"


def test_overdue_status():
    assert calculate_status(
        estimated_cents=100000,
        paid_cents=0,
        due_date="2026-01-01",
        as_of=date(2026, 6, 1),
    ) == "OVERDUE"


def test_remaining_balance_never_negative():
    assert remaining_balance(100000, 120000) == 0
