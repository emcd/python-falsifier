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


''' Assert correct integration of classcore for immutability. '''


import pytest

import falsifier


def test_falsifier_module_is_immutable():
    ''' Test that the falsifier module itself is immutable. '''
    with pytest.raises(AttributeError):
        falsifier.new_attribute = "test"
    with pytest.raises(AttributeError):
        del falsifier.Falsifier # Try deleting an existing attribute

def test_falsifier_class_is_immutable():
    ''' Test that classes within Falsifier (e.g., Falsifier class) are immutable. '''
    with pytest.raises(AttributeError):
        falsifier.Falsifier.new_method = lambda x: x
    # Check for an existing attribute if possible, e.g., a dunder method
    # For example, attempting to delete __repr__ might be too disruptive or protected.
    # Instead, let's try to change a known attribute if one existed that was meant to be class-level mutable before.
    # Given Falsifier is simple, we'll focus on adding new attributes.

def test_falsifier_object_instance_attributes_are_not_immutable_by_default_classcore():
    ''' Test that Falsifier object instances do not become immutable by default.
        classcore's reclassify_modules typically makes the *module* and *classes* immutable.
        Instance-level immutability would require specific classcore decorators on the Falsifier class itself.
    '''
    obj = falsifier.Falsifier()
    try:
        obj.some_new_attr = 123
        assert obj.some_new_attr == 123
    except AttributeError:
        pytest.fail("Instances of Falsifier should be mutable by default after classcore.reclassify_modules.")
