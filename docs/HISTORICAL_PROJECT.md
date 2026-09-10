# Historical Project Record — CSIT 555 Group 5

## Course and submission

- **Course:** CSIT 555_01 SP24 — Database Systems
- **Instructor:** Prof. Xiaofeng Li
- **Submission:** Final Project — Group 5
- **Date:** April 27, 2024

## Verified team

The submitted project document lists:

- Dianah Mutanda
- Michael Gluck
- Noah Mengich
- Perps Ndiege
- Sarah Bober
- Sarmad Sohail

## Historical project objective

The team designed a software system for a fictional New Jersey company, Group 5 LLC, to calculate and track tax-payment information and persist records in a database. The report describes a web UI that displays and inserts database values and captures quarterly estimated-tax obligations.

## Original repository

`https://github.com/migluck/csit555final`

## Historical functionality evidenced by the report

The submitted report contains sections/screenshots for:

- tax-payment system home page
- tabular records
- tax-rate / summary field
- tax-breakdown filtering
- create operation
- read operation
- update operation
- delete operation
- payment and reporting controllers
- viewing/updating payment information in the database
- add-payment endpoint
- payment-record listing endpoint
- backend database connection
- SQL schema

The report identifies the local application endpoints as:

```text
http://localhost:8001/add
http://localhost:8001
```

These endpoint statements describe the submitted historical system; they are not the current portfolio application's route contract.

## Architecture recovered from Git history

The original repository's branch and commit history provides additional architectural evidence beyond the final report. During development, the system included a multi-container design using Flask, MySQL, and Docker Compose.

A fuller stage of the architecture contained:

```text
Browser / Client
      |
      v
Reporting Service
      |
      | HTTP
      v
Payment Record Service ---> MySQL
      ^
      |
Tax Calculation Service
```

An earlier design also contained Nginx as a reverse proxy. Later commits simplified and reintegrated services, so the exact architecture changed over the project's lifecycle.

## Historical technology evidence

- Python
- Flask
- Flask-SQLAlchemy
- MySQL
- Docker
- Docker Compose
- HTML/CSS
- JavaScript UI behavior
- REST/HTTP service communication
- relational schema design
- CRUD operations

## Attribution statement

The Group 5 final report establishes that **Perps Ndiege was a member of the six-person team**. It does not identify a line-by-line individual contribution matrix.

The surviving Git history visibly attributes commits to accounts including `migluck`, `Decabra`, and `woods9msu`. For that reason, this portfolio treats the original system as a **team-developed academic project** and does not assign specific historical components to Perps Ndiege without additional evidence.

## Relationship to this repository

The current `PerpsAkach/tax-payment-tracker` repository is not represented as a byte-for-byte copy of the 2024 source. It is a modern portfolio reconstruction and extension that preserves the verified domain while improving portability, monetary representation, data modeling, validation, and documentation.

See the root `README.md` and `PROVENANCE.md` for current implementation details.