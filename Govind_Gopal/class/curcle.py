
from circle_class import Circle
rad = []
def main_menu():
	print(Circle.__doc__)
	print ("Enter your choice")
	print ("1.Enter new radius")
	print ("2.Enter radius to compute area")
	print ("3. Add two radius")
	print ("4. Display using String Function") 
	print ("5.EXit")
while True:
	main_menu()
	ch = input("Enter your choice")
	if ch == "1":
		radius = int(input("\t\tEnter the radius"))
		rad.append(Circle(radius))
	elif ch == "2":
		for i in rad:
			print(f"\t\t{i.radius}")
		radius = int(input("\t\tenter the radius to compute"))
		x = list(filter(lambda a: a.radius == radius,rad))		
		print(x)
		for i in x:
			print(i.area())
	
	
	elif ch== "3":
		for i in rad:
			print(f"\t\t{i.radius}")
		r1=Circle(int(input("Enter the first radius")))
		r2=Circle(int(input("Enter the second radius")))
		c=r1+r2
		print(c)
	
	
	elif ch== "4":
		for i in rad:
			print(f"\t\t{i.radius}")
		r1=Circle(int(input("Enter the first radius")))
		print(str(r1))
	
	
	elif ch == "5":
		break
		
	else:
		print("Invalid input")	
