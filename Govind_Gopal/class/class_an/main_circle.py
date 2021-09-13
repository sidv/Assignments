
from circle import Circle


rad=[]
def main_menu():
	print("1. Adding Radius!!")
	print("2. Computing Area!!!")
	print("3. display document")
	print("4. Display Radius List")
	print("5. Display using String Function") 
	print("6. Add new radius")
	print("7. Exit")

while True:
	main_menu()
	
	ch = int(input("Enter your choice"))
	if ch == 1:
		radius=int(input("Enter the radius"))
		st_temp = Circle(radius)
		rad.append(st_temp)
		

	elif ch == 2:
		
		for i in rad:
			print(f"{i.radius}")
		r=int(input("Enter the radius to compute area:"))	
		x=list(filter(lambda a: a.radius == r,rad))
		#print(x)
		#print("Anju")
		#print(x[0])
		for i in x:
			r=Circle(r)
			print(r.area())
	elif ch== 3:
		print(Circle.__doc__)
	elif ch== 4:
		for i in rad:
			print(f"{i.radius}")
	elif ch== 5:
		#pass
		r1=Circle(10)
		print(str(r1))
	elif ch== 6:
		r1=Circle(5)
		r2=Circle(6)
		c=r1+r2
		print(c)
	
	elif ch == 7:
		
		break;
	else:
		print("Invalid Choice")



