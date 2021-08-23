from sedan import Sedan
from suv import SUV

all_sedan = []
all_suv = []
#car= { sedans: [] ,suv : []}
def menu():
	print("Press 1 to add sedan")
	print("Press 2 to add suv")
	print("Press 3 to display sedan")
	print("Press 4 to display SUV")
	print("Press 5 to get sedan classs in built attributes/functions ")
while True:
	menu()
	ch = int(input("Choice: "))
	if ch == 1:
		#add to sedan
		all_sedan.append(Sedan())
		all_sedan[-1].insert()
	elif ch == 2:
		#add to suv
		all_suv.append(SUV())
		all_suv[-1].insert()
	elif ch == 3:
		for i in all_sedan:
			i.display()
	elif ch == 4:
		#display suv
		for i in all_suv:
			i.display()
	elif ch == 5:
		a= Sedan()
		b = Sedan()
		a.insert()
		print(dir(a))
		print(Sedan.__name__) #Classname.inbuilt attribute
		print(a.__doc__)
		print(Sedan.__bases__)
		print(len(a))
		print(str(a))
		b.insert()
		c = a + b
		print(c)
#		e1= Employee()
#		e2= Employee()
#		e3= Employee()
#		total_salary = e1.salary+e2.salary+e3.salary
# 		total_salary = e1+e2+e3+e4
#		e1+e2
#		e1==name
	else:
		print("Invalid choice")
