# Grid Connection Analysis Automation

Automate power flow calculations and grid integration impact studies for Distributed Generation (DG) power plants to validate, contest, and minimize the financial impact of network upgrade requirements issued by utilities.

## Core Objective
Strictly validate utility grid connection proposals and identify opportunities to avoid unnecessary network upgrades (re-conductoring, substation expansions) by proving the existing grid infrastructure compliance with ANEEL's **PRODIST Módulo 8** standards (specifically steady-state voltage deviation limits: $0.95 \le V_{pu} \le 1.05$).

## Project Structure
- `src/bdgd_tools/`: Parser and tools for ANEEL's Base de Dados Geográfica da Distribuidora (BDGD).
  - `core/models.py`: Pydantic Data Transfer Objects (DTOs) for grid assets.
  - `core/gdb_parser.py`: High-performance File Geodatabase parser using GeoPandas and pyogrio.
- `tests/`: Automated unit and integration tests.
- `docs/`: Comprehensive documentation and implementation plans.
- `data/`: Placeholder for BDGD File Geodatabase (.gdb) inputs (not committed to git).

## Setup & Installation

This project uses Python >= 3.10. Install the package in editable mode with test dependencies:

```bash
pip install -e ".[test]"
```

## Running Tests
Run tests using pytest:
```bash
pytest
```

## Documentation Index
For detailed technical documentation, refer to:
- [System Architecture](docs/architecture.md) — Decoupled design, GDBParser, and Pydantic models.
- [Regulatory Framework](docs/regulatory.md) — PRODIST Módulo 8 details and grid compliance checks.
- [Development Guide](docs/development.md) — Mentorship rules, coding standards, and repository workflows.
