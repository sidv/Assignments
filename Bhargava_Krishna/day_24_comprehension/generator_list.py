def sqr_num():
	for i in range(10,25):
		yield i
		
x = sqr_num()
print(x)
print(type(x))
y = list(map(lambda a: a*a,x))
print(y)
