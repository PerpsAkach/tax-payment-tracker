# Tax Payment Tracker

Flask and SQLite web application for tracking quarterly payment records, partial payments, balances, annual summaries, and CSV exports.

## Features

- Year and quarter records
- Jurisdiction field
- Multiple payments per tracked period
- Integer-cent monetary storage
- Payment status calculation
- Annual reporting
- CSV export
- SQLite persistence
- Flask/Jinja interface
- Automated tests

## Run

```bash
pip install -r requirements.txt
flask --app run.py init-db
flask --app run.py seed-db
flask --app run.py run --debug
```

This repository is a portfolio reconstruction of the original Flask/SQLite CRUD project. See `PROVENANCE.md` for implementation provenance.
