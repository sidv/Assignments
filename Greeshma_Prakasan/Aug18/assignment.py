def ran():
	for i in range(1000,3001,2):
		if i==3000:	
			print(i)
		else:
			print(i,end=",")

#ran()

def even_sq():
	l = [1,2,3,4,5,6,7,8,9,10]
	li = list(map(lambda a:a*a,filter(lambda a:a%2==0,l)))
	print(li)

even_sq()
