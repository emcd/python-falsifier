# falsifier

Falsifier provides a base class for creating falsey objects — objects that
evaluate to `False` in boolean contexts while maintaining distinct identities.
It serves as a building block for sentinel objects, absence indicators, and
custom falsey types where `None` or `False` may be semantically meaningful.

## Architectural Goals

**Minimalism**
   Single public class with no runtime configuration, no complex inheritance,
   and no state management beyond object identity.

**Composability**
   Users subclass `Falsifier` to create domain-specific types. No enforced
   patterns or constraints on usage.

**Protocol Compatibility**
   Implements standard Python object protocols (bool, hash, comparison,
   string) for seamless integration with builtins and collections.

## Architecture

### Core Module

Location: `classes.py`

The single `Falsifier` class implements:

- **Boolean protocol**: `__bool__` returns `False`
- **Hashing protocol**: `__hash__` uses `id(self)` for identity-based hashing
- **Comparison protocol**: `__eq__`/`__ne__` use identity comparison;
  `__lt__`, `__le__`, `__gt__`, `__ge__` return `NotImplemented`
- **String protocols**: `__str__` returns `'False_'`; `__repr__` returns the
  fully-qualified class name

### Identity-Based Semantics

The core pattern uses object identity (`id()`) for both hashing and equality:

- Each instance is unique by default
- Instances are comparable only to themselves
- Enables use in sets and as dictionary keys

### Import Hub

Location: `__/`

The `__` subpackage provides centralized imports:

- `imports.py`: External library imports (`classcore`, `typing_extensions`,
  `dynadoc`)
- `nomina.py`: Type aliases (`ComparisonResult`, `NominativeArguments`,
  `PositionalArguments`) and naming constants
- `__init__.py`: Re-exports for package-wide access

### Package Entry Point

Location: `__init__.py`

Exports the public API:

- Imports and re-exports `Falsifier` from `classes` module
- Finalizes module using `classcore.standard.finalize_module`
- Maintains `__version__`

## Dependencies

- `classcore`: Provides `qualify_class_name` for `__repr__` and module
  finalization
- `dynadoc`: Documentation infrastructure
- `typing_extensions`: Cross-version type annotation support

## Filesystem Organization

```
sources/
└── falsifier/
    ├── __/                  # Centralized import hub
    │   ├── __init__.py      # Re-exports imports and nomina
    │   ├── imports.py       # External library imports
    │   └── nomina.py        # Type aliases and naming constants
    ├── __init__.py          # Package entry point
    ├── classes.py           # Falsifier class implementation
    └── py.typed             # Type checking marker (PEP 561)
```
