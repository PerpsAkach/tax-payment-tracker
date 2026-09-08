from __future__ import annotations

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def dollars_to_cents(value) -> int:
    try:
        amount = Decimal(str(value).replace(",", "").replace("$", "").strip())
    except (InvalidOperation, AttributeError) as exc:
        raise ValueError("Invalid monetary amount") from exc

    if not amount.is_finite():
        raise ValueError("Amount must be finite")

    amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return int(amount * 100)


def cents_to_dollars(cents: int) -> Decimal:
    return (Decimal(int(cents)) / Decimal(100)).quantize(Decimal("0.01"))


def format_money(cents: int) -> str:
    return f"${cents_to_dollars(cents):,.2f}"
