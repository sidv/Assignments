def even():
	for i in range(10,25):
		yield i
		
x = even()
print(type(x))
y = list(filter(lambda a : a%2 == 0, x))
print(y)
