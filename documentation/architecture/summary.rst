.. vim: set fileencoding=utf-8:
.. -*- coding: utf-8 -*-
.. +--------------------------------------------------------------------------+
   |                                                                          |
   | Licensed under the Apache License, Version 2.0 (the "License");          |
   | you may not use this file except in compliance with the License.         |
   | You may obtain a copy of the License at                                  |
   |                                                                          |
   |     http://www.apache.org/licenses/LICENSE-2.0                           |
   |                                                                          |
   | Unless required by applicable law or agreed to in writing, software      |
   | distributed under the License is distributed on an "AS IS" BASIS,        |
   | WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. |
   | See the License for the specific language governing permissions and      |
   | limitations under the License.                                           |
   |                                                                          |
   +--------------------------------------------------------------------------+


*******************************************************************************
System Overview
*******************************************************************************

The ``falsifier`` library provides a single-class architecture focused on
minimal complexity and maximum extensibility. It implements a foundational
base class for creating falsey objects with identity-based semantics.

Architectural Principles
===============================================================================

Minimalism
-------------------------------------------------------------------------------

The library maintains a deliberately minimal surface area:

* Single public class (``Falsifier``)
* No complex inheritance hierarchies
* No runtime configuration
* No state management beyond object identity

This minimalism ensures:

* **Predictable behavior**: No hidden state or complex interactions
* **Easy integration**: Minimal impact on consuming codebases
* **Low maintenance burden**: Fewer components to maintain and test

Composability
-------------------------------------------------------------------------------

The ``Falsifier`` class serves as a building block rather than a complete
solution:

* Users subclass to create domain-specific types
* No enforced patterns or constraints on usage
* Compatible with standard Python object protocols

Dependency Management
-------------------------------------------------------------------------------

Dependencies are carefully selected:

* ``classcore``: Provides ``qualify_class_name`` utility for ``__repr__``
* ``dynadoc``: Supports documentation infrastructure
* ``typing_extensions``: Enables type annotations across Python versions

These dependencies align with the project's ecosystem and provide essential
utilities without adding complexity.

System Components
===============================================================================

Core Module: ``falsifier.classes``
-------------------------------------------------------------------------------

**Location:** ``sources/falsifier/classes.py``

Contains the single ``Falsifier`` class implementing:

**Boolean Protocol:**
    ``__bool__`` returns ``False`` to enable falsey semantics

**Hashing Protocol:**
    ``__hash__`` uses ``id(self)`` for identity-based hashing

**String Protocols:**
    - ``__str__`` returns ``'False_'`` for simple representation
    - ``__repr__`` returns fully-qualified class name for debugging

**Comparison Protocol:**
    - ``__eq__`` uses identity comparison (``self is other``)
    - ``__ne__`` uses identity comparison (``self is not other``)
    - ``__lt__``, ``__le__``, ``__gt__``, ``__ge__`` return ``NotImplemented``

Import Hub: ``falsifier.__``
-------------------------------------------------------------------------------

**Location:** ``sources/falsifier/__/``

Implements the standard ``__`` subpackage pattern for centralized imports:

* ``imports.py``: External library imports (``classcore``, ``typing_extensions``, etc.)
* ``nomina.py``: Type aliases (``ComparisonResult``, etc.) and naming constants
* ``__init__.py``: Re-exports for package-wide access

This pattern provides:

* Consistent import interface across all modules
* Centralized dependency management
* Namespace isolation from individual modules

Package Entry Point: ``falsifier.__init__``
-------------------------------------------------------------------------------

**Location:** ``sources/falsifier/__init__.py``

Exports the public API:

* Imports and re-exports ``Falsifier`` from ``classes`` module
* Finalizes module using ``classcore`` standard finalization
* Maintains version information

Data Flow
===============================================================================

The library has no runtime data flow - it provides class definitions only:

1. User imports ``Falsifier`` class
2. User instantiates ``Falsifier`` or derived class
3. Instance responds to Python protocols (``bool()``, ``hash()``, ``==``, etc.)
4. No internal state changes or side effects occur

Deployment Architecture
===============================================================================

Distribution
-------------------------------------------------------------------------------

The library is distributed as a pure Python package:

* Single wheel for all platforms
* No compiled extensions
* No runtime dependencies beyond specified packages

Integration Patterns
-------------------------------------------------------------------------------

**Direct Usage:**
    Import ``Falsifier`` and instantiate for immediate use

**Subclassing:**
    Derive custom classes with specialized behavior

**Singleton Pattern:**
    Users implement module-level singletons as needed (see examples)

Key Architectural Patterns
===============================================================================

Identity-Based Semantics
-------------------------------------------------------------------------------

The core pattern uses object identity (``id()``) for both hashing and
equality:

* Each instance is unique by default
* Instances are comparable only to themselves
* Enables use in sets and as dictionary keys

This pattern aligns with Python's behavior for object instances and provides
predictable semantics without additional complexity.

Protocol-Based Extensibility
-------------------------------------------------------------------------------

The class implements Python's standard object protocols:

* Boolean protocol for falsey behavior
* Hashing protocol for collection usage
* Comparison protocol for equality checks
* String protocols for representation

Subclasses inherit these protocols and can override as needed while
maintaining compatibility with Python's builtin operations.

Type Annotation Strategy
-------------------------------------------------------------------------------

The library uses ``typing_extensions`` for cross-version compatibility:

* ``TypeAlias`` for custom type definitions
* ``Any`` for unrestricted types in comparison methods
* Return type annotations on all public methods

This enables static type checking while maintaining runtime compatibility
across Python versions.

Error Handling Philosophy
===============================================================================

The library follows a "fail-fast" approach:

* Ordered comparisons return ``NotImplemented`` (not exceptions)
* No custom exception types (none needed for current functionality)
* Let Python's type system and protocols handle invalid usage

This minimizes error handling code and relies on Python's established
conventions.