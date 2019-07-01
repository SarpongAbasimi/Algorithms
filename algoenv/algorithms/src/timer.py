from datetime import datetime

class Timer():
  
  def build(self,list_size):
    if type(list_size) == str:
      return []
    return [i for i in range(1, list_size)]
  
  def calculate_time(self, a_list, algorithm):
    start_time = datetime.now()
    algorithm(a_list)
    print(datetime.now() - start_time)
    return(datetime.now() - start_time)
