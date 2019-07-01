import sys, os, pytest
current_path = os.path.dirname(__file__)
sys.path.insert(0, current_path + '/../')
from lib.algorithms import MyAlgorithms


@pytest.fixture()
def instantian_alorithim():
    reverse_algo = MyAlgorithms()
    return reverse_algo

class TestMyAlgorithms:
    def test_reverse_method_returns_a_list_if_passed_a_string(self, instantian_alorithim):
        assert instantian_alorithim.reverse_('s') == []

    def test_reverse_method_reverses_elements_in_list(self, instantian_alorithim):
        assert instantian_alorithim.reverse_([1,2]) == [2,1]
    
    def test_reverse_method_reverses_many_elements_in_list(self, instantian_alorithim):
        normal_list = [4,6,8,3,6,0,2,1,5,6,7]
        reversed_list = [7, 6, 5, 1, 2, 0, 6, 3, 8, 6, 4]
        assert instantian_alorithim.reverse_(normal_list) == reversed_list
    
    def test_duplicate_method_returns_an_empty_array_if_no_duplicate(self, instantian_alorithim):
        list_with_out_duplicates = [1,2,4]
        assert instantian_alorithim.duplicate_(list_with_out_duplicates) == []

    def test_duplicate_method_returns_duplicates_in_array_if_any(self, instantian_alorithim):
        list_with_out_duplicates = [1,2,4,4]
        assert instantian_alorithim.duplicate_(list_with_out_duplicates) == [4]

    def test_duplicate_method_returns_duplicates_in_array_if_any(self, instantian_alorithim):
        list_with_out_duplicates = [1,2,4,4,4,5,5,5,5,5,6,6,6,6]
        assert instantian_alorithim.duplicate_(list_with_out_duplicates) == [4,5,6]

        



