from random import shuffle

class BuiltInAlgorithms():

  def reverse_list(self, a_list):
    a_list.reverse()
    return a_list
  
  def do_sort(self, a_list):
    a_list.sort()
    return a_list
  
  def do_shuffle(self, a_list):
    shuffle(a_list)
