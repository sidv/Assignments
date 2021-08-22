
import change_emp as c
import search_emp as s
import team as t
import Employees as e
import org as o

employees = {} #empty List
organization = {}
teams = {}

def main_menu():
	print("1. Add employee")
	print("2. Delete employee")
	print("3. Search employee")
	print("4. Display all employee")
	print("5. Change a employee name in the list") 
	print("6.Manage all groups")
	print("7.Manage organization details")
	print("8. exit")

while True:
	main_menu()
	ch = int(input("Enter your choice: "))
	if ch is None:
		print("no data present in Employees")
	elif ch == 1:
		#Add employee
		e.add_employee()
	elif ch == 2:
		#Delete employee
		e.delete_employee()
	elif ch == 3:
		#Search employee
		#s.search_employee()
		s.search_employee_lambda()
	elif ch == 4:
		#Display employee
		e.display_employee()
	elif ch== 5:
		#Change a employee name in the list
		c.change_employee()
	elif ch== 6:
		#Manage all groups in the list
		t.manage_all_teams()
	elif ch== 7:
		#Manage all organizations in the list
		o.manage_all_organizations()
		
	elif ch == 8:
		#Exit
		break;
	else:
		print("Invalid Choice")
		

