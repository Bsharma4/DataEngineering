import pytest
from transformations import *

@pytest.mark.parametrize("value,expected", [
    ('cat','cat'),
    ('dog','dog'),
    ('CAT','cat'),
    (None,None)])
def test_type(value,expected):
    assert transform_type(value) == expected