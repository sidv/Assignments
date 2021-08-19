from fruit_store import fruits
import fruit_func as ff

while True:
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add fruit
		ff.add_fruit()
	elif ch == 2:
		#Delete fruit
		ff.delete_fruit()
	elif ch == 3:
		#Display fruits
		ff.display_fruits()
	else:
		print("Invalid Choice")

