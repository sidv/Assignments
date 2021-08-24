"""

def square_num(num):
	return num*num
my_list =list(range(10,50))
update=map(square_num,my_list)
print(list(update))
"""



sq_map = list(range(10,50))
res =list(map(lambda x : x*x ,sq_map))
print(res)
