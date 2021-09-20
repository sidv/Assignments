from emp_class import Employee 
from emp_store import employees

import add as ad
import del_emp as de
import search_emp as se
import display_emp as dis
import update_emp as ue

def main_menu():
	print("Press 1 for add employee")
	print("Press 2 for delete employee ")
	print("Press 3 for search employee")
	print("Press 4 for change employee details")
	print("Press 5 for display  employee")
	print("Press 6 for Quit")

while True:
	
	main_menu()
	ch = int(input("Enter choice"))
	if ch == 1:
		ad.add_employee()
	elif ch == 2:
		de.delete_employee()
	elif ch == 3:
		se.search_employee()
	elif ch == 4:
		ue.update_employee()	
	elif ch == 5:
		dis.display_employee()
	elif ch == 6:
		break;
	else:
		print("Invalid Choice")
