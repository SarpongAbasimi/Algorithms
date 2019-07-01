import sys, os
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_path + '/../')

from lib.timer import Timer 
from lib.in_built import BuiltInAlgorithms


timer = Timer()
inbuilt_algorithm = BuiltInAlgorithms()

timer.calculate_time(timer.build(100), inbuilt_algorithm.reverse_list)
timer.calculate_time(timer.build(100), inbuilt_algorithm.do_shuffle)
timer.calculate_time(timer.build(100), inbuilt_algorithm.do_sort)