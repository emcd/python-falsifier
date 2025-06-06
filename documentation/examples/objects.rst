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


Objects
===============================================================================

The ``falsifier.classes`` module provides the ``Falsifier`` class, which serves
as a base for creating objects that evaluate to ``False`` in boolean contexts.

Basic Usage
-------------------------------------------------------------------------------

The ``Falsifier`` class can be used directly to create falsey objects:

.. doctest:: Falsifier

    >>> from falsifier import Falsifier
    >>> obj = Falsifier( )
    >>> bool( obj )  # Always evaluates to False
    False
    >>> str( obj )   # Simple string form
    'False_'
    >>> repr( obj )  # Detailed representation
    'falsifier.classes.Falsifier( )'

Identity and Equality
-------------------------------------------------------------------------------

Instances of ``Falsifier`` use identity-based comparison, making each instance
unique:

.. doctest:: Falsifier

    >>> obj1 = Falsifier( )
    >>> obj2 = Falsifier( )
    >>> obj1 == obj2  # Different instances are never equal
    False
    >>> obj1 == obj1  # Same instance equals itself
    True
    >>> obj1 is obj2  # Different instances have different identity
    False

.. note::

   Ordered comparisons (``<``, ``<=``, ``>``, ``>=``) on ``Falsifier``
   instances are not supported and will raise ``TypeError`` if attempted.

Deriving Custom Types
-------------------------------------------------------------------------------

The ``Falsifier`` class is particularly useful as a base for creating custom
falsey types:

.. doctest:: Falsifier

    >>> class AbsentValue( Falsifier ):
    ...     ''' Represents an explicitly absent value. '''
    ...
    ...     def __str__( self ) -> str:
    ...         return 'absent'
    >>>
    >>> absent = AbsentValue( )
    >>> bool( absent )  # Inherits falsey behavior
    False
    >>> str( absent )   # Custom string representation
    'absent'

Creating Singletons
-------------------------------------------------------------------------------

``Falsifier`` can be used to create singleton falsey objects at the module
level:

.. doctest:: Falsifier

    >>> from falsifier import Falsifier
    >>>
    >>> # Module-level singleton
    >>> _undefined_instance = None
    >>>
    >>> def get_undefined( ):
    ...     ''' Returns the singleton undefined instance. '''
    ...     global _undefined_instance
    ...     if _undefined_instance is None:
    ...         class Undefined( Falsifier ):
    ...             ''' Represents an undefined value. '''
    ...             def __str__( self ) -> str:
    ...                 return 'undefined'
    ...         _undefined_instance = Undefined( )
    ...     return _undefined_instance
    >>>
    >>> undefined = get_undefined( )
    >>> undefined2 = get_undefined( )
    >>> undefined is undefined2  # Same instance
    True
    >>> bool( undefined )       # Still falsey
    False

Collection Usage
-------------------------------------------------------------------------------

``Falsifier`` instances are uniquely hashable, making them suitable for use in
sets or as dictionary keys:

.. doctest:: Falsifier

    >>> obj1 = Falsifier( )
    >>> obj2 = Falsifier( )
    >>> unique_falseys = { obj1, obj2, obj1 }  # Set deduplicates by identity
    >>> len( unique_falseys )
    2
    >>> obj1 in unique_falseys
    True
    >>>
    >>> falsey_map = { obj1: 'first', obj2: 'second' }
    >>> falsey_map[ obj1 ]
    'first'
