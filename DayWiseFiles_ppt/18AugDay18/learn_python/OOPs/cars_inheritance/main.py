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
	else:
		print("Invalid choice")
