# 8.Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# method 1
def ret_list(lst):
    return list(set(lst))


lst = [1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 9]
print(ret_list(lst))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# method 2
lst = [1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(set(map(lambda a: a, lst))))
