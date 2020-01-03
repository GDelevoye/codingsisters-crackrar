import os
import pytest


@pytest.fixture
def rootdir():
    return os.path.dirname(os.path.abspath(__file__))

def test_brute_force_pin(rootdir):
    pass
