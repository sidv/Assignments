#5.Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
num = [1,2,3,4,5,6,7,8,9,10]

lst = list(filter(lambda a:a%2 ==0,num))
print(lst)
lst_map = list(map(lambda a : a*a,lst))
print(lst_map)
