from __future__ import annotations

import os
from pathlib import Path

from flask import Flask, jsonify, request

from .db import Database
from .money import dollars_to_cents
from .services import calculate_status, remaining_balance


def create_app(database_path: str | None = None) -> Flask:
    app = Flask(__name__)
    path = database_path or os.getenv("DATABASE_PATH", str(Path(app.instance_path) / "tax_tracker.db"))
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    db = Database(path)
    db.initialize()
    app.extensions["tax_tracker_db"] = db

    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok"})

    @app.post("/api/periods")
    def create_period():
        data = request.get_json(force=True)
        try:
            year = int(data["tax_year"])
            quarter = int(data["quarter"])
            estimated = dollars_to_cents(data["estimated_amount"])
            jurisdiction = str(data["jurisdiction"]).strip()
            due_date = str(data["due_date"]).strip()
        except (KeyError, TypeError, ValueError) as exc:
            return jsonify({"error": "invalid_period"}), 400

        if quarter not in {1, 2, 3, 4} or not jurisdiction:
            return jsonify({"error": "invalid_period"}), 400

        with db.transaction() as conn:
            cursor = conn.execute(
                """
                INSERT INTO tax_periods
                    (tax_year, quarter, jurisdiction, estimated_amount_cents, due_date, notes)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (year, quarter, jurisdiction, estimated, due_date, data.get("notes")),
            )
            period_id = cursor.lastrowid

        return jsonify({"id": period_id}), 201

    @app.get("/api/periods")
    def list_periods():
        with db.connect() as conn:
            rows = conn.execute(
                "SELECT * FROM tax_periods ORDER BY tax_year DESC, quarter ASC"
            ).fetchall()
            items = []
            for row in rows:
                paid = conn.execute(
                    "SELECT COALESCE(SUM(amount_cents),0) AS total FROM payments WHERE tax_period_id = ?",
                    (row["id"],),
                ).fetchone()["total"]
                items.append({
                    "id": row["id"],
                    "tax_year": row["tax_year"],
                    "quarter": row["quarter"],
                    "jurisdiction": row["jurisdiction"],
                    "estimated_amount_cents": row["estimated_amount_cents"],
                    "paid_cents": int(paid),
                    "remaining_cents": remaining_balance(row["estimated_amount_cents"], int(paid)),
                    "status": calculate_status(
                        estimated_cents=row["estimated_amount_cents"],
                        paid_cents=int(paid),
                        due_date=row["due_date"],
                    ),
                })
        return jsonify({"items": items})

    @app.post("/api/periods/<int:period_id>/payments")
    def add_payment(period_id: int):
        data = request.get_json(force=True)
        try:
            amount = dollars_to_cents(data["amount"])
            payment_date = str(data["payment_date"]).strip()
        except (KeyError, TypeError, ValueError):
            return jsonify({"error": "invalid_payment"}), 400

        if amount <= 0:
            return jsonify({"error": "invalid_payment"}), 400

        with db.transaction() as conn:
            exists = conn.execute("SELECT id FROM tax_periods WHERE id = ?", (period_id,)).fetchone()
            if exists is None:
                return jsonify({"error": "period_not_found"}), 404
            cursor = conn.execute(
                """
                INSERT INTO payments
                    (tax_period_id, payment_date, amount_cents, payment_method, confirmation_number, notes)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    period_id,
                    payment_date,
                    amount,
                    data.get("payment_method"),
                    data.get("confirmation_number"),
                    data.get("notes"),
                ),
            )
            payment_id = cursor.lastrowid
        return jsonify({"id": payment_id}), 201

    return app
