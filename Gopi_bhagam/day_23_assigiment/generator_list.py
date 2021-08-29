def square_num():
	for i in range(10,50):
		yield i
x = square_num()
print(type(x))
res=list(map(lambda a : a*a , x))
print(res)


print('===========================compreshensiom==================')

print([x*x for x in range(10,50)])

print([x for x in map (lambda x : x*x ,range(10,51))])

