from datetime import datetime


class Timer:
    def build_list_of_size(self, list_size):
        if type(list_size) is str: return []

        built_list_size = []
        for i in range(1, list_size):
            built_list_size.append(i)
        return built_list_size
    
    def cal_time(self, a_list, algorithm):
        print(datetime.now().time())
        algorithm(a_list)
        print(datetime.now().time())






def reverse_(a_list):
    return a_list.reverse()


timer = Timer()

print( timer.cal_time([2,3,4,5,6], reverse_)   )