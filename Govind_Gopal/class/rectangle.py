from redtangle_class import Rectangle
lengths = []
def main_menu():
	print(Rectangle.__doc__)
	print ("Enter your choice")
	print ("1.Enter new measurements")
	print ("2.Choose the measurements to compute area")
	print ("3. Add two lengths ")
	#print ("5. Display using String Function") 
	print ("6.EXit")


while True:
	main_menu()
	ch = input("Enter your choice")
	if ch == "1":
		length = int(input("\t\tEnter the length"))
		breadth = int(input("\t\tEnter the breadth"))
		lengths.append(Rectangle(length,breadth))
	elif ch == "2":
		for i in lengths:
			print(f"\t\tChoices are {i.length} X {i.breadth}")
		length = int(input("\t\tenter the length to compute"))
		breadth = int(input("\t\tenter the breadth to compute"))
		x = list(filter(lambda a: a.length == length and a.breadth == breadth,lengths))

		for i in x:
			print(i.area())

	elif ch == "3":
		for i in lengths:
			print(f"\t\tChoices are {i.length} X {i.breadth}")
		l1 = int(input("Enter the first length to add"))
		l2 = int(input("Enter the second length to add"))
		b1 = int(input("Enter the first breadth to add"))
		b2 = int(input("Enter the second breadth to add"))
		rec1 = Rectangle(l1,b1)
		rec2 = Rectangle(l2,b2)
		#c = l1 + l2
		#d = b1 + b2
		s = rec1+rec2
		print( f"The sums are {s}")


	elif ch == "6":
		break
		
	else:
		print("Invalid input")	
