# Design Document: Modular Documentation Structure

## Purpose
Establish a robust, modular documentation structure that ensures clear onboarding, defines the regulatory limits of the system, details the Clean Architecture design, and ensures that documentation remains synchronized with code throughout development.

## Scope
1. Update `GEMINI.md` system instructions to include documentation update checks in the development cycle.
2. Create a comprehensive root `README.md`.
3. Scaffold modular documentation files:
   - `docs/architecture.md`: Software architecture, DTOs, and separation of concerns.
   - `docs/regulatory.md`: Regulatory rules (PRODIST Módulo 8) and technical stance.
   - `docs/development.md`: Guidelines, mentorship rules, and coding standards.

## Target Outlines

### 1. Root `README.md`
- **Project Overview:** High-level description of grid connection impact analysis.
- **Key Features:** What the tool can do.
- **Directory Layout:** Project file tree.
- **Installation & Setup:** How to install using python package tools (uv, pip, virtualenv).
- **Test Commands:** Running unit tests with pytest.
- **Documentation Index:** Navigation links to `docs/` files.

### 2. `docs/architecture.md`
- **Clean Architecture Principles:** Separation of concerns between parsing (.gdb parsing via GeoPandas/pyogrio) and simulation (OpenDSSDirect.py).
- **Intermediary DTOs:** Role of Pydantic models for data validation and decoupling.
- **Data Flow Diagram:** Mermaid representation of ingestion -> validation -> simulation.

### 3. `docs/regulatory.md`
- **ANEEL PRODIST Módulo 8:** Steady-state voltage limits ($0.95 \le V_{pu} \le 1.05$).
- **Defense Philosophy:** Objective verification of capacity to avoid utility-driven network upgrades.

### 4. `docs/development.md`
- **Mentorship Cycle:** Overview of user-driven execution, code review, and active learning.
- **Style Guides:** PEP 8, 100% type annotations, Sphinx-style docstrings.
- **Documentation Integration:** Rules for updating docs as part of feature development.
