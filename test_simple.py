import pytest
import os

def test_simple_add():
    assert 1 + 1 == 2

@pytest.mark.skipif(os.name == 'posix', reason='does not run on mac')
def test_simple_sub():
    assert 1 - 1 == 0