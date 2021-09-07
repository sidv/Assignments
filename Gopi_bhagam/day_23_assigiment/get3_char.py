def get_char(x):
	for i in x:
		yield i[0:3]
x=["Siddhant","Pavan","Ramya","Raja"]
res=get_char(x)
print(type(res))
print(res)
y=list(map(lambda a :a[0:3],x))
print(y)


print('++++++++++++++++++++++++++++compreshension++++++++++++++++++++++++++')



print([x[0:3] for x in ["Siddhant","Pavan","Ramya","Raja"]])
