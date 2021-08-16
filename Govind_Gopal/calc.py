while True:

	a = int(input("Enter the first number \n"))
	b = int(input("Enter the second number \n"))
	numb = int(input("Enter your option \n 1. addition \n 2. subtraction \n 3. multiplication \n 4. division \n 5. Break \n"))



	if numb == 1 :
		c = a + b
		print ("The sum is {}".format(c))
	elif numb == 2 :
		c = a - b
		print ("The difference is {}".format(c))
	elif numb == 3 :
		c = a * b
		print ("The product is {}".format(c))
	elif numb == 4 :
		c = a / b 
		print ("The result is {}".format(c))
	elif numb == 5 :
		break

	else:
		print ("Invalid input")


