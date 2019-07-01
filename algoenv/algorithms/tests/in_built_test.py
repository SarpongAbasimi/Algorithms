import os, sys, pytest 

CURRENTPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENTPATH + '/../')

from lib.in_built import BuiltInAlgorithms

@pytest.fixture()
def algo():
  algo = BuiltInAlgorithms
  return algo 

class TestBuiltInAlgorithms(object):

  def test_reverse(self, algo):
    input_list = [1,2,3]
    assert algo.reverse_list(self, input_list) == [3,2,1]
