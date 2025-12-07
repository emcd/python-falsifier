# Project Context

## Purpose
`falsifier` is a simple Python library that provides a base class for falsey objects—objects that evaluate to `False` in boolean contexts. It is designed to create unique sentinel objects or absence indicators where `None` or `False` might be valid values, ensuring identity-based equality.

## Tech Stack
- **Language**: Python >= 3.10
- **Build System**: Hatch (backend: `hatchling`)
- **Linting & Formatting**: Ruff, Isort
- **Type Checking**: Pyright
- **Testing**: Pytest, Coverage
- **Documentation**: Sphinx
- **Changelog Management**: Towncrier

## Project Conventions

### Code Style
- **Line Length**: 79 characters.
- **Indentation**: 4 spaces.
- **Linting**: Strict adherence to Ruff rules configured in `pyproject.toml` (includes Flake8, Pylint, etc.).
- **Imports**: Sorted by `isort` with 79 char line length.
- **Filesystem Organization**: See [Filesystem Organization](../filesystem.rst) for details on the root, source, test, and documentation structure.

### Architecture Patterns
- **Minimalism & Composability**: Single public class (`Falsifier`) with no complex hierarchy or state. See [System Overview](../summary.rst) for architectural principles.
- **Import Hub Pattern**: Uses a `__` subpackage (`sources/falsifier/__/`) for centralized imports and project-wide definitions (`nomina.py`).
- **Identity-Based Semantics**: Uses object identity for hashing and equality.

### Testing Strategy
- **Framework**: Pytest.
- **Structure**: Tests mirror source code structure under `tests/`.
- **Naming**: Numeric prefixes for test modules (e.g., `test_000_package.py`) and functions to control execution order.
- **Coverage**: 100% branch coverage target.
- **Doctests**: Run via Sphinx.

### Git Workflow
- **Changelog**: Managed by `towncrier`. Changes must include a fragment in `.auxiliary/data/towncrier`.
- **Commits**: Should reference changelog fragments where appropriate.

## Domain Context
- **Falsey Objects**: Objects where `bool(obj)` is `False`.
- **Sentinel Objects**: Unique markers for states like "Not Set" or "Missing".
- **Identity Equality**: `obj == obj` is True, `obj == other` is False (unless `other is obj`).

## Important Constraints
- **Python Version**: Must support Python 3.10 through 3.14.
- **Dependencies**: Relies on `classcore` and `dynadoc`.
- **No Compiled Extensions**: Pure Python package.

## External Dependencies
- **classcore**: For class factories and decorators.
- **dynadoc**: For documentation generation.
- **typing-extensions**: For type hints compatibility.
