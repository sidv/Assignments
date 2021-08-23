import group as g
import organization as o
import employee as e

while True:
	
	e.main_menu()
	ch = int(input("Enter your choice"))
	if ch == 1:
		o.org_details()
	elif ch == 2:
		e.add_employee()
	elif ch == 3:
		e.delete_employee()
	elif ch == 4:
		e.search_employee()
	elif ch== 5:
		e.display_employee 
	elif ch == 6:
		e.change_employee_details()
	elif ch == 7:
		t.manage_groups()
	elif ch ==8:
		#Exit
		break;
	else:
		print("Invalid Choice")

