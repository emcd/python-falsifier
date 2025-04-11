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

:tocdepth: 4


*******************************************************************************
API
*******************************************************************************


Package ``falsifier``
===============================================================================

A base class for creating objects that evaluate to ``False`` in boolean
contexts. This functionality is useful for creating sentinel objects, absence
indicators, and other specialized falsey types that need distinct identities
and proper comparison behavior.

* ``Falsifier``: A base class that produces objects which evaluate to ``False``
  in boolean contexts. Each instance has a unique identity and supports proper
  equality comparison and hashing.


Module ``falsifier.objects``
-------------------------------------------------------------------------------

.. automodule:: falsifier.objects
