from lib.in_built_algorithms import Algorithms


class TestAlgorithms():
    def test_sort(self):
        algorithm = Algorithms()
        input_list = [1,2,3,4,5]
        assert algorithm.do_reverse(input_list) == [5,4,3,2,1]