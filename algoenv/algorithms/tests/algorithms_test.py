import sys, os, pytest, random
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + '/../')

from src.algorithms import Algorithms

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
  
  def test_reverse_slice_method(self, algorithm):
    assert algorithm.reverse_slice_([1,3]) == [3,1]
    assert algorithm.reverse_slice_('s')  == []
  
  def test_duplicate_returns_list_when_pass_string(self, algorithm):
    assert algorithm.duplicate_('s') == []
  
  def test_duplicate_returns_duplicates_in_list(self, algorithm):
    assert algorithm.duplicate_([1,2,1]) == [1]
  
  def test_duplicate_returns_duplicates_in_list(self, algorithm):
    assert algorithm.duplicate_([1,2,1,2,3,3,3,3,4,4,4,1,4]) == [1, 2, 3, 4]
  
  def test_last_in_list(self, algorithm):
    assert algorithm.last([1, 2]) == 2
    assert algorithm.last([1, 2, 5, 6]) == 6