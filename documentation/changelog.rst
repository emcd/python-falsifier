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
Release Notes
*******************************************************************************


.. towncrier release notes start


Falsifier 2.0 (2024-12-20)
==========================

Deprecations and Removals
-------------------------

- Remove immutability on ``Falsifier`` class as it may cause metaclass
  conflicts on derived classes. Developers may use a separate mixin, such as
  ``frigid.ImmutableObject`` to achieve immutability on derived classes.


Falsifier 1.0 (2024-12-15)
==========================

Features
--------

- Add ``Falsifier`` base class for creating objects that evaluate to ``False``
  in boolean contexts. Each instance has a unique identity, supports proper
  equality comparison and hashing, and can be used in collections like sets and
  dictionaries.


Supported Platforms
-------------------

- Add support for CPython 3.10 to 3.13.
- Add support for PyPy 3.10.
