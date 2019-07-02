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
  
  def duplicate_(self, a_list):
    duplicates = []
    if type(a_list) != list:
      return []
    for i in a_list:
      if a_list.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
    return duplicates
  
