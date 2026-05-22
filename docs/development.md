# Developer Guide & Coding Standards

This project is structured as a learning repository following a strict mentorship model.

## Mentorship Workflow
All development is user-driven. The agent provides designs, instructions, and exact terminal commands, and the user executes them.

## Coding Standards

### 1. Style & Guidelines
- Strict adherence to **PEP 8** style guidelines.
- 4-space indentation.

### 2. Type Hinting
- 100% type hinting using the native `typing` module or Python 3.10+ native pipe syntax.
- No implicit or explicit `Any` types without solid documentation.

### 3. Documentation Style
- All modules, classes, and methods must have comprehensive Google or Sphinx-style docstrings.
- Docstrings must list:
  - **Parameters** (with types and descriptions)
  - **Raises** (exceptions thrown)
  - **Returns** (types and descriptions)

### 4. Continuous Documentation Rule
Before marking any implementation task as complete, the corresponding documentation must be reviewed and updated. Ensure links are kept fully updated.
