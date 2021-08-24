employees = {} #empty List
import Employees as e

def change_employee():
	#Change a employee detailes
	print("\t Enter 1 for change name")
	print("\t Enter 2 for change age ")
	print("\t Enter 3 for change gender ")
	print("\t Enter 4 for change salary ")

	choice = int(input("\tEnter the choice which u want to change: "))
	serial_no = input("\tEnter serial no: ")
	if choice == 1:
		e.employees[serial_no]['name'] = input("\tEnter new name: ")
	elif choice == 2:
		e.employees[serial_no]['age'] = input("\tEnter new age: ")
	elif choice == 3:
		e.employees[serial_no]['gender'] = input("\tEnter new gender: ")
	elif choice == 4:
		e.employees[serial_no]['salary'] = input("\tEnter new salary: ")
	#else:
		#print("\t invalid choice")
