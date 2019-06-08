from lib.algorithms import MyAlgorithms

class TestMyAlgorithms:
    def test_reverse_method_returns_a_list_if_passed_a_string(self):
        reverse_algo = MyAlgorithms()
        assert reverse_algo.reverse_('s') == []

    def test_reverse_method_reverses_elements_in_list(self):
        reverse_algo = MyAlgorithms()
        assert reverse_algo.reverse_([1,2]) == [2,1]
    
    def test_reverse_method_reverses_many_elements_in_list(self):
        reverse_algo = MyAlgorithms()
        assert reverse_algo.reverse_([4,6,8,3,6,0,2,1,5,6,7]) == [7, 6, 5, 1, 2, 0, 6, 3, 8, 6, 4]
