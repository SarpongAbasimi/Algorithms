import sys, os
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_path + '/../')

from src.timer import Timer 
from src.in_built import BuiltInAlgorithms
from src.algorithms import Algorithms


timer = Timer()
algorithm = Algorithms()
inbuilt_algorithm = BuiltInAlgorithms()

timer.calculate_time(timer.build(100), inbuilt_algorithm.reverse_list)
timer.calculate_time(timer.build(100), inbuilt_algorithm.do_shuffle)
timer.calculate_time(timer.build(100), inbuilt_algorithm.do_sort)

print('**********')
timer.calculate_time(timer.build(10000), algorithm.reverse_)
print('**********')
timer.calculate_time(timer.build(10000), algorithm.reverse_slice_)
print('**********')
timer.calculate_time(timer.build(10000), inbuilt_algorithm.reverse_list)