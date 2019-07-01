import sys, os, pytest
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + '/../')

from lib.algorithms import Algorithms

@pytest.fixture
def algorithm():
  algorithm = Algorithms()
  return algorithm

class TestAlgorithms(object):

  def test_reverse(self, algorithm):
    assert algorithm.reverse_([1, 5]) == [5, 1]
    assert algorithm.reverse_([2, 10, 6, 7, 9, 4]) == [4, 9, 7, 6, 10, 2]
  
  def test_that_it_returns_list_if_passed_string(self, algorithm):
    assert algorithm.reverse_('s')  == []

