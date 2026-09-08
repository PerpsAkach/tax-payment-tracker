from __future__ import annotations

from datetime import date


def calculate_status(*, estimated_cents: int, paid_cents: int, due_date: str, as_of: date | None = None) -> str:
    today = as_of or date.today()
    due = date.fromisoformat(due_date)
    remaining = max(0, estimated_cents - paid_cents)

    if estimated_cents == 0:
        return "NO AMOUNT TRACKED"
    if remaining == 0:
        return "PAID"
    if today > due:
        return "OVERDUE"
    if paid_cents > 0:
        return "PARTIALLY PAID"
    return "UNPAID"


def remaining_balance(estimated_cents: int, paid_cents: int) -> int:
    return max(0, estimated_cents - paid_cents)
