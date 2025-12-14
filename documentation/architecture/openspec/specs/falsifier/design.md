# Falsifier Design

## Context
The library is designed to provide a standard way to create falsey objects with identity. It avoids the overhead and complexity of more feature-rich libraries when simple sentinel values are needed.

## Goals
- Provide a `Falsifier` class that behaves like `False` but has distinct identity.
- Ensure compatibility with Python standard object protocols.
- Maintain minimal runtime overhead.

## Non-Goals
- **Singleton management**: Users implement singleton patterns themselves.
- **Immutability guarantees**: Base class does not enforce immutability.
- **Ordered comparisons**: `<` and `>` operations are explicitly not supported.
- **Serialization support**: No built-in pickle or JSON serialization.
- **Thread safety mechanisms**: Users handle concurrency as needed.

## Technical Decisions

### Decision: Identity-based Hashing
- **Decision**: Use `id(self)` for `__hash__`.
- **Rationale**: Ensures that each instance is treated as unique in sets and dictionary keys, consistent with `object` default behavior but explicit for clarity.

### Decision: Explicit Falsey Behavior
- **Decision**: Implement `__bool__` to return `False`.
- **Rationale**: This is the core purpose of the library.

### Decision: Minimal Dependencies
- **Decision**: Depend only on Python standard library, `classcore` (for utilities), `dynadoc` (documentation), and `typing_extensions`.
- **Rationale**: Keep the library lightweight and easy to install.

## Non-Functional Requirements

### Minimal Dependencies
The library depends only on:
- Python standard library
- `classcore`
- `dynadoc`
- `typing_extensions`

### Type Annotation Support
All public APIs include complete type annotations compatible with `mypy` and `pyright`.

### Cross-Version Compatibility
The library supports all actively maintained Python versions (currently 3.10+).

### Zero Runtime Overhead
The `Falsifier` class imposes minimal runtime overhead beyond basic object creation costs.
