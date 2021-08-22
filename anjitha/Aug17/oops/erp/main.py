from employee import Employee 
from emp_store import employees
import search as s
import change_emp as change

def main_menu():
	print("1. Add employee")
	print("2. Delete employee")
	print("3. Search employee")
	print("4. Display all employee")
	print("5. Change a employee details") 
	print("6. exit")

while True:
	main_menu()
	
	ch = int(input("Enter your choice"))
	if ch == 1:
		e_id = input("\tEnter employee id : ")
		name = input("\tEnter name : ")
		age = input("\tEnter employee age : ")
		gender = input("\tEnter gender : ")
		place = input("\tEnter place : ")
		salary = input("\tEnter salary : ")
		previous_company = input("\tEnter previous company : ")
		joining_date = input("\tEnter joining_date : ")

		st_temp = Employee(e_id,name,age,gender,place,salary,previous_company,joining_date)
		employees.append(st_temp)

	elif ch == 2:
		
		eid=input("Enter the employye id:")
		for i in employees:
			if i.empid == eid:
				employees.pop(employees.index(i))
		
	elif ch == 3:
		s.search_main()
			
		
	elif ch == 4:
		for i in employees:
			print(f"{i.name} | {i.age} | {i.gender} | {i.place} | {i.salary}| {i.previous_company} | {i.joining_date}")
	elif ch== 5:
		change.change_main()
	
	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")

























