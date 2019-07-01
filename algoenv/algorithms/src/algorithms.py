class Algorithms():
  def reverse_(self,a_list):

    reversed_array = []
    counter = len(a_list) - 1

    if type(a_list) == str:
        return []
    while counter >= 0:
        reversed_array.append(a_list[counter])
        counter -= 1
    return reversed_array

  def reverse_slice_(self, a_list):
    return [] if type(a_list) == str else a_list[::-1]
  
