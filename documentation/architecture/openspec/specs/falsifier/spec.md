# Falsifier

## Purpose
The `falsifier` library provides a minimal, focused foundation for creating falsey objects in Python that maintain distinct identities. It serves developers who need sentinel values, absence indicators, or custom falsey types where `None` or `False` may be semantically meaningful values.

## Requirements

### Requirement: Boolean Evaluation
The `Falsifier` class SHALL implement `__bool__` to return `False`.

Priority: Critical

#### Scenario: Boolean context
- **WHEN** a `Falsifier` instance is used in a boolean context
- **THEN** it evaluates to `False`

### Requirement: Identity-Based Hashing
The `Falsifier` class SHALL implement `__hash__` using object identity (`id(self)`).

Priority: High

#### Scenario: Hashing
- **WHEN** `hash()` is called on a `Falsifier` instance
- **THEN** it returns the integer identity of the object

### Requirement: String Representations
The `Falsifier` class SHALL provide distinct string representations.

Priority: Medium

#### Scenario: String conversion
- **WHEN** `str()` is called on a `Falsifier` instance
- **THEN** it returns `'False_'`

#### Scenario: Representation
- **WHEN** `repr()` is called on a `Falsifier` instance
- **THEN** it returns the fully qualified class name with empty call syntax

### Requirement: Equality Comparison
The `Falsifier` class SHALL implement identity-based equality comparison.

Priority: Critical

#### Scenario: Identity equality
- **WHEN** a `Falsifier` instance is compared to itself using `==`
- **THEN** it returns `True`

#### Scenario: Distinct object inequality
- **WHEN** a `Falsifier` instance is compared to a different instance using `==`
- **THEN** it returns `False`

#### Scenario: Inequality operator
- **WHEN** a `Falsifier` instance is compared to a different instance using `!=`
- **THEN** it returns `True`

### Requirement: Ordered Comparison Rejection
The `Falsifier` class SHALL implement `__lt__`, `__le__`, `__gt__`, and `__ge__` to return `NotImplemented`.

Priority: Low

#### Scenario: Less than comparison
- **WHEN** a `Falsifier` instance is compared using `<`
- **THEN** it raises `TypeError` (assuming other operand returns `NotImplemented`)

### Requirement: Subclass Compatibility
The `Falsifier` class SHALL support subclassing without requiring special metaclass machinery.

Priority: Medium

#### Scenario: Creating a subclass
- **WHEN** a class inherits from `Falsifier`
- **THEN** instances of the subclass evaluate to `False`
- **AND** instances of the subclass maintain distinct identity
