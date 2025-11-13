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
Filesystem Organization
*******************************************************************************

This document describes the specific filesystem organization for the project,
showing how the standard organizational patterns are implemented for this
project's configuration. For the underlying principles and rationale behind
these patterns, see the `common architecture documentation
<https://raw.githubusercontent.com/emcd/python-project-common/refs/tags/docs-1/documentation/common/architecture.rst>`_.

Project Structure
===============================================================================

Root Directory Organization
-------------------------------------------------------------------------------

The project implements the standard filesystem organization:

.. code-block::

    python-falsifier/
    ├── LICENSE.txt              # Project license
    ├── README.rst               # Project overview and quick start
    ├── pyproject.toml           # Python packaging and tool configuration
    ├── documentation/           # Sphinx documentation source
    ├── sources/                 # All source code
    ├── tests/                   # Test suites
    └── .auxiliary/              # Development workspace

Source Code Organization
===============================================================================

Package Structure
-------------------------------------------------------------------------------

The main Python package follows the standard ``sources/`` directory pattern:

.. code-block::

    sources/
    └── falsifier/               # Main Python package
        ├── __/                  # Centralized import hub
        │   ├── __init__.py      # Re-exports imports and nomina
        │   ├── imports.py       # External library imports
        │   └── nomina.py        # Type aliases and naming constants
        ├── __init__.py          # Package entry point
        ├── classes.py           # Falsifier class implementation
        └── py.typed             # Type checking marker (PEP 561)

All package modules use the standard ``__`` import pattern as documented
in the common architecture guide.

Import Hub Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``__`` subpackage provides centralized imports:

**imports.py**
    Imports from external libraries:

    * ``collections.abc`` as ``cabc`` - Abstract base classes for containers
    * ``types`` - Standard Python types module
    * ``classcore.utilities`` as ``ccutils`` - Class utility functions
    * ``classcore.standard`` as ``ccstd`` - Module finalization utilities
    * ``dynadoc`` - Documentation support
    * ``typing_extensions`` as ``typx`` - Type annotation support

**nomina.py**
    Project-specific type aliases and constants:

    * ``ComparisonResult`` - Union type for comparison return values
    * ``NominativeArguments`` - Type alias for keyword arguments
    * ``PositionalArguments`` - Type alias for positional arguments
    * ``package_name`` - Runtime package name extraction

**__init__.py**
    Re-exports all symbols from ``imports`` and ``nomina`` for convenient
    access throughout the package.

Module Organization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**classes.py**
    Contains the single ``Falsifier`` class with all protocol implementations.
    This is currently the only feature module as the library maintains minimal
    scope.

**__init__.py**
    Package entry point that:

    * Imports the ``__`` subpackage for access to utilities
    * Exports ``Falsifier`` from ``classes`` module
    * Defines ``__version__`` for runtime version access
    * Calls ``ccstd.finalize_module`` for standard module finalization

Test Organization
===============================================================================

Test Structure
-------------------------------------------------------------------------------

Tests follow the standard mirror structure:

.. code-block::

    tests/
    └── test_000_falsifier/      # Test suite for falsifier package
        ├── __init__.py          # Test package marker
        ├── __.py                # Test-specific imports and utilities
        ├── conftest.py          # Pytest configuration and fixtures
        ├── test_000_package.py  # Package-level tests
        ├── test_010_base.py     # Base functionality tests
        └── test_100_classes.py  # Falsifier class tests

The ``test_000_falsifier`` directory mirrors the ``sources/falsifier`` package
structure. Test modules use numeric prefixes to control execution order.

Documentation Organization
===============================================================================

Documentation Structure
-------------------------------------------------------------------------------

.. code-block::

    documentation/
    ├── _static/                     # Static assets for Sphinx
    ├── architecture/                # Architecture documentation
    │   ├── decisions/               # Architectural decision records
    │   │   └── index.rst
    │   ├── designs/                 # Design documents
    │   │   └── index.rst
    │   ├── testplans/               # Test planning documents
    │   │   ├── index.rst
    │   │   └── summary.rst
    │   ├── filesystem.rst           # This file
    │   ├── index.rst                # Architecture index
    │   └── summary.rst              # System overview
    ├── examples/                    # Usage examples
    │   ├── index.rst
    │   └── objects.rst              # Falsifier usage examples
    ├── api.rst                      # Public API reference
    ├── changelog.rst                # Release changelog
    ├── conf.py                      # Sphinx configuration
    ├── contribution.rst             # Contribution guidelines
    ├── devapi.rst                   # Development API reference
    ├── index.rst                    # Documentation home
    ├── license.rst                  # License information
    └── prd.rst                      # Product requirements

Development Workspace
===============================================================================

The ``.auxiliary/`` directory (created by agentsmgr) contains development
resources:

.. code-block::

    .auxiliary/
    ├── instructions/                # Development guidelines
    │   ├── architecture.rst         # Architecture documentation guide
    │   ├── nomenclature.rst         # Naming conventions
    │   └── [other guides]           # Additional development guides
    ├── notes/                       # Session notes and TODOs
    └── scribbles/                   # Temporary development files

This workspace is excluded from package distributions via ``.gitignore``.

Configuration Files
===============================================================================

Root-level configuration files:

* ``pyproject.toml`` - Python packaging, tool configuration (pytest, ruff, etc.)
* ``LICENSE.txt`` - Apache License 2.0
* ``README.rst`` - Project overview and quick start guide

The project uses ``pyproject.toml`` as the single source of configuration for
all development tools, following PEP 518 and modern Python packaging standards.
