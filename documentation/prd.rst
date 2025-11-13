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
Product Requirements Document
*******************************************************************************

Vision
===============================================================================

The ``falsifier`` library provides a minimal, focused foundation for creating
falsey objects in Python that maintain distinct identities. It serves
developers who need sentinel values, absence indicators, or custom falsey
types where ``None`` or ``False`` may be semantically meaningful values.

Target Audience
===============================================================================

Primary Users
-------------------------------------------------------------------------------

* **Library developers** creating packages that need custom sentinel values or
  absence indicators with falsey semantics
* **Application developers** implementing domain-specific falsey types for
  state machines, validators, or data processing pipelines
* **Framework authors** building systems requiring distinct falsey markers

User Stories
===============================================================================

Core Functionality
-------------------------------------------------------------------------------

**Story 1: Create Falsey Objects**

    As a library developer, I want to create objects that evaluate to
    ``False`` in boolean contexts so that I can represent absence or
    invalidity while maintaining object identity.

    **Acceptance Criteria:**

    * Objects instantiated from ``Falsifier`` evaluate to ``False`` with ``bool()``
    * Objects maintain distinct identities via ``id()``
    * Objects are usable in conditional expressions

**Story 2: Identity-Based Equality**

    As a developer, I want falsey objects to use identity-based comparison so
    that each instance is unique and distinguishable.

    **Acceptance Criteria:**

    * Instances compare equal only to themselves (``obj == obj`` is ``True``)
    * Different instances are never equal (``obj1 == obj2`` is ``False``)
    * Identity checks work correctly (``obj is obj`` is ``True``)

**Story 3: Hashable Instances**

    As a developer, I want falsey objects to be hashable so that I can use
    them in sets and as dictionary keys.

    **Acceptance Criteria:**

    * Instances are hashable via identity-based hashing
    * Instances can be added to sets without errors
    * Instances can be used as dictionary keys

**Story 4: Derive Custom Types**

    As a developer, I want to subclass ``Falsifier`` to create
    domain-specific falsey types with custom string representations.

    **Acceptance Criteria:**

    * Subclasses inherit falsey behavior
    * Subclasses can override ``__str__`` and ``__repr__``
    * Subclasses maintain identity-based equality

Non-Goals
===============================================================================

The library explicitly does not provide:

* **Singleton management**: Users implement singleton patterns themselves
* **Immutability guarantees**: Base class does not enforce immutability
* **Ordered comparisons**: ``<``, ``<=``, ``>``, ``>=`` operations are not supported
* **Serialization support**: No built-in pickle or JSON serialization
* **Thread safety mechanisms**: Users handle concurrency as needed

Functional Requirements
===============================================================================

FR-1: Boolean Evaluation
-------------------------------------------------------------------------------

The ``Falsifier`` class shall implement ``__bool__`` to return ``False``.

FR-2: Identity-Based Hashing
-------------------------------------------------------------------------------

The ``Falsifier`` class shall implement ``__hash__`` using object identity
(``id(self)``).

FR-3: String Representations
-------------------------------------------------------------------------------

The ``Falsifier`` class shall provide:

* ``__str__`` returning ``'False_'``
* ``__repr__`` returning the fully qualified class name with empty call syntax

FR-4: Equality Comparison
-------------------------------------------------------------------------------

The ``Falsifier`` class shall implement:

* ``__eq__`` returning ``self is other``
* ``__ne__`` returning ``self is not other``

FR-5: Ordered Comparison Rejection
-------------------------------------------------------------------------------

The ``Falsifier`` class shall implement ``__lt__``, ``__le__``, ``__gt__``,
and ``__ge__`` to return ``NotImplemented``.

FR-6: Subclass Compatibility
-------------------------------------------------------------------------------

The ``Falsifier`` class shall support subclassing without requiring special
metaclass machinery.

Non-Functional Requirements
===============================================================================

NFR-1: Minimal Dependencies
-------------------------------------------------------------------------------

The library shall depend only on:

* Python standard library
* ``classcore`` for utility functions
* ``dynadoc`` for documentation support
* ``typing_extensions`` for type annotations

NFR-2: Type Annotation Support
-------------------------------------------------------------------------------

All public APIs shall include complete type annotations compatible with
``mypy`` and ``pyright``.

NFR-3: Cross-Version Compatibility
-------------------------------------------------------------------------------

The library shall support all actively maintained Python versions (currently
3.9+).

NFR-4: Zero Runtime Overhead
-------------------------------------------------------------------------------

The ``Falsifier`` class shall impose minimal runtime overhead beyond basic
object creation costs.