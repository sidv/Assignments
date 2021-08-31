while True:

	giv_num=int(input("Enter required number:\n"))
	giv_range=int(input("Enter required range:\n"))
	
	i=1
	while i< (giv_range+1):
		print(str(i)+"x"+str(giv_num)+" = "+str(giv_num*i))
		i=i+1
	print(" ")
