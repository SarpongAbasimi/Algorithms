from datetime import datetime
from algorithms import MyAlgorithms

class Timer:
    def build_list_of_size(self, list_size):
        if type(list_size) is str: return []

        built_list_size = []
        for i in range(1, list_size):
            built_list_size.append(i)
        return built_list_size
    
    def cal_time(self, a_list, algorithm):
        start_time = datetime.now()
        algorithm(a_list)
        return(datetime.now() - start_time)

timer = Timer()
algo = MyAlgorithms()

print(timer.cal_time([1,2,3,4,5,6], algo.reverse_))