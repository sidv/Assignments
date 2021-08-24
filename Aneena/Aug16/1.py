a_list = list(range(10,51))
print("_______The list is_______\n : ")
print(a_list)

a_list1=map(lambda a: a * a, a_list)
print("*****Square of all numbers*****\n")
print(list(a_list1))

a_list1=list(filter(lambda a : a%2 == 0,a_list))
print("*****All even numbers from the list******\n :")
print(a_list1)
