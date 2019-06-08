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
        
    def duplicate_(self, a_list):
        duplicates = []
        if type(a_list) != list:
            return []
        for i in a_list:
            if a_list.count(i) > 1 and i not in duplicates:
                duplicates.append(i)
        return duplicates
        



a = MyAlgorithms()
print(a.duplicate_([1,3,4,5,5]))