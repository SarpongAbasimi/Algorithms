from lib.timer import Timer

class TestTimer:

    def test_when_passed_sting_empty_list(self):
        timer = Timer()
        assert timer.build_list_of_size('s') == []

    def test_build_list_of_size_two(self):
        timer = Timer()
        assert timer.build_list_of_size(3) == [1,2]
    
    def test_build_list_of_size_three(self):
        timer = Timer()
        assert timer.build_list_of_size(10) == [1,2,3,4,5,6,7,8,9]


