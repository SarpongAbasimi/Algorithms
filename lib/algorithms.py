print('I was just called')
class MyAlgorithms:
    def reverse_(self, a_list):
        reversed_array = []
        if type(a_list) == str:
            return []
        counter = len(a_list) - 1
        while counter >= 0:
            reversed_array.append(a_list[counter])
            counter -= 1
        return reversed_array


