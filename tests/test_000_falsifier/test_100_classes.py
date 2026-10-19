# vim: set filetype=python fileencoding=utf-8:
# -*- coding: utf-8 -*-

#============================================================================#
#                                                                            #
#  Licensed under the Apache License, Version 2.0 (the "License");           #
#  you may not use this file except in compliance with the License.          #
#  You may obtain a copy of the License at                                   #
#                                                                            #
#      http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                            #
#  Unless required by applicable law or agreed to in writing, software       #
#  distributed under the License is distributed on an "AS IS" BASIS,         #
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#  See the License for the specific language governing permissions and       #
#  limitations under the License.                                            #
#                                                                            #
#============================================================================#


''' Assert correct function of Falsifier class. '''


import pytest

from .__ import PACKAGE_NAME, cache_import_module

MODULE_QNAME = f"{PACKAGE_NAME}.classes"


def test_100_instantiation( ):
    ''' Class instantiates. '''
    module = cache_import_module( MODULE_QNAME )
    obj = module.Falsifier( )
    assert isinstance( obj, module.Falsifier )


def test_101_boolean_evaluation( ):
    ''' Object evaluates to False. '''
    module = cache_import_module( MODULE_QNAME )
    obj = module.Falsifier( )
    assert not obj
    assert False == bool( obj ) # noqa: E712


def test_102_equality( ):
    ''' Object equality is identity-based. '''
    module = cache_import_module( MODULE_QNAME )
    obj1 = module.Falsifier( )
    obj2 = module.Falsifier( )
    assert obj1 == obj1
    assert obj1 != obj2
    assert not (obj1 == obj2) # noqa: SIM201


def test_103_hash_uniqueness( ):
    ''' Object hashes are unique. '''
    module = cache_import_module( MODULE_QNAME )
    obj1 = module.Falsifier( )
    obj2 = module.Falsifier( )
    assert hash( obj1 ) != hash( obj2 )
    assert hash( obj1 ) == hash( obj1 )


def test_104_string_representations( ):
    ''' Object has expected string representations. '''
    module = cache_import_module( MODULE_QNAME )
    obj = module.Falsifier( )
    assert 'False_' == str( obj )
    assert f'{MODULE_QNAME}.Falsifier( )' == repr( obj )


def test_105_ordering_operations( ):
    ''' Object does not support ordering. '''
    module = cache_import_module( MODULE_QNAME )
    obj1 = module.Falsifier( )
    obj2 = module.Falsifier( )
    with pytest.raises( TypeError ):
        _ = obj1 < obj2
    with pytest.raises( TypeError ):
        _ = obj1 <= obj2
    with pytest.raises( TypeError ):
        _ = obj1 > obj2
    with pytest.raises( TypeError ):
        _ = obj1 >= obj2


def test_106_collection_usage( ):
    ''' Object works in collections. '''
    module = cache_import_module( MODULE_QNAME )
    obj1 = module.Falsifier( )
    obj2 = module.Falsifier( )
    unique_set = { obj1, obj2, obj1 }
    assert 2 == len( unique_set )
    assert obj1 in unique_set
    assert obj2 in unique_set
    mapping = { obj1: 'first', obj2: 'second' }
    assert 'first' == mapping[ obj1 ]
    assert 'second' == mapping[ obj2 ]


def test_900_docstring_sanity( ):
    ''' Class has valid docstring. '''
    module = cache_import_module( MODULE_QNAME )
    assert hasattr( module.Falsifier, '__doc__' )
    assert isinstance( module.Falsifier.__doc__, str )
    assert module.Falsifier.__doc__
