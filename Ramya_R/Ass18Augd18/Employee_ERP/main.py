from employee import Employee #If you are importing the class here directly you dont need to write the modulename.classname
#from modulename import classname/function/variable

import search_emp as s
import change_emp as c
from employee_list import employees

#employees = []

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
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add employee
		emp_id = input("\tEnter employee id : ")
		name = input("\tEnter name: ")
		age = int(input("\tEnter age: "))
		gender = input("\tEnter the Gender: ")
		place =  input("\tEnter place: ")
		salary = input("\tEnter salary: ")
		prev_company = input("\tEnter previous company: ")
		join_date = input("\tEnter join date: ")
		

		emp_temp = Employee(emp_id,name,age,gender,place,salary,prev_company,join_date)
		employees.append(emp_temp)

	elif ch == 2:
		#Delete employee
		emp_id = input("\tEnter employee id: ")
		for i in employees:
			if i.emp_id == emp_id:
				employees.remove(i)
				print("Deleted successfully")
		#pass
	elif ch == 3:
		#Search employee
		s.search_employee()
	elif ch == 4:
		#Display employee
		for i in employees:
			print(f"{i.name} | {i.age} | {i.gender} | {i.place} | {i.salary} | {i.prev_company} | {i.join_date} | {self.get_username()} | {self._role}")
			print("Found Employees")
		
	elif ch== 5:
		#Change a employee details
		c.change_employee()
	elif ch == 6:
		#Manage groups
		pass
	elif ch == 7:
		#Manage organizations
		pass
	elif ch == 8:
		#Exit
		break;
	else:
		print("Invalid Choice")

























