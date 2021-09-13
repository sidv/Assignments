import math
a = []
def seq():
	for i in range(10,51):
		yield i
for i in seq():
	a.append(i)
print (a)
b = list(map(lambda x: math.pow(x,2) ,a))
print(b)
c = list(filter(lambda x: x%2 == 0, a))
print(c)
