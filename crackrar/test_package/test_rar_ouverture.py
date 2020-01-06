import os
import pytest

from crackrar.rar_ouverture import essayer_mdp

@pytest.fixture
def rootdir():
    return os.path.dirname(os.path.abspath(__file__))

def test_essayer_mdp(rootdir):
    path_to_file = os.path.join(rootdir,'testdata/notes.rar')
    assert essayer_mdp(path_to_file, mdp="1789") == True
    assert essayer_mdp(path_to_file,mdp=1789) == True
    assert essayer_mdp(path_to_file,mdp="abcd") == False
    assert essayer_mdp(path_to_file,"1789","notes1") == True
    assert essayer_mdp(path_to_file,1789,"notes1") == True
    assert essayer_mdp(path_to_file,"abcgd","notes1") == False
    assert essayer_mdp(path_to_file,1899,"notes2") == False
