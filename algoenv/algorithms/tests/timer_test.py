import os, sys, pytest 

CURRENTPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENTPATH + '/../')

from lib.timer import Timer

@pytest.fixture()
def timer():
  timer = Timer()
  return timer

class TestTimer(object):

  def test_returns_a_list_if_size_is_a_string(self, timer):
    assert timer.build('s') == []
  
  def test_returns_list_of_size_2_if_given_3(self, timer):
    assert timer.build(3) == [1,2]
  
  def test_returns_list_of_size_20_if_given_21(self, timer):
    assert len(timer.build(21)) == 20
