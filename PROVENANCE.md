# Provenance

## RECOVERED — verified historical team project

The original project is verified by the Spring 2024 **CSIT 555_01 — Database Systems** Group 5 final-project document dated April 27, 2024.

That document identifies the six-person team as:

- Dianah Mutanda
- Michael Gluck
- Noah Mengich
- Perps Ndiege
- Sarah Bober
- Sarmad Sohail

It also links the original public repository:

`https://github.com/migluck/csit555final`

Recovered historical project facts include:

- Flask-based application/services
- MySQL relational database
- Docker and Docker Compose
- tax/payment record tracking
- web UI
- create/read/update/delete workflows
- payment and reporting controllers
- database schema
- quarterly estimated-tax tracking requirements
- service-to-service integration during development
- reporting and filtering behavior

The original Git history also shows that the architecture evolved across branches and commits, including a fuller multi-service design with tax-calculation, payment-record, reporting, and an earlier Nginx reverse-proxy configuration.

## ATTRIBUTION BOUNDARY

The historical project documentation proves **team membership**, not individual authorship of every source file.

The surviving Git commit history visibly attributes substantial implementation work to other team Git identities, including `migluck`, `Decabra`, and `woods9msu`. Therefore this portfolio does not claim that Perps Ndiege individually authored the entire historical codebase or any specific historical component unless separate evidence establishes that fact.

## RECONSTRUCTED

The current code in this repository is a portfolio reconstruction of the verified tax-payment tracking domain.

Current reconstruction choices include:

- Flask application structure
- portable SQLite persistence
- explicit TaxPeriod and Payment entities
- user-entered due dates
- current route/service organization

SQLite is **not** presented as the historical database. The historical team implementation used MySQL.

## ENHANCED

Modern portfolio improvements include:

- parent-child TaxPeriod → Payment relational modeling
- integer-cent monetary storage
- Decimal-based money parsing
- support for multiple partial payments
- derived status logic
- annual reporting
- CSV export
- validation and database constraints
- testable service-layer organization
- explicit historical/current architecture documentation

## UNVERIFIED

Unless additional evidence is recovered, the following are not asserted as historical individual facts:

- which specific historical files were personally authored by Perps Ndiege
- exact division of labor among all six team members
- whether every planned microservice remained in the final submitted runtime
- exact production/deployment behavior beyond the surviving source and final-project documentation

## Evidence hierarchy

1. Original CSIT 555 Group 5 final-project document — strongest evidence for course, project, team membership, requirements, screenshots, and repository identity.
2. Original public Git repository and commit/branch history — strongest evidence for source architecture and version evolution.
3. Current portfolio implementation — evidence only for the present reconstruction/enhancements, not for historical individual authorship.
