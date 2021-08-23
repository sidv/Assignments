from emp_store import employees

def change_menu():
	print("1. Change by name")
	print("2. Change by age")
	print("3. Change by salary")
	print("4. Change by gender")
	print("5. exit")


def change_main():	
	while True:
		change_menu()
		choi=int(input("Enter your choice"))
		if choi == 1:
			e_id = input("Enter Employee id: ")
			st_temp  = list(filter(lambda a: a.empid == e_id,employees))
			st_temp[0].set_name(input("Enter new name: "))
		elif choi == 2:
			age = input("Enter Employee id: ")
			st_temp  = list(filter(lambda a: a.age == age,employees))
			st_temp[0].set_age(input("Enter new age: "))
		elif choi == 3:
			salary = input("Enter Employee id: ")
			st_temp  = list(filter(lambda a: a.salary == salary,employees))
			st_temp[0].set_salary(input("Enter new salary: "))
		elif choi == 4:
			gender = input("Enter Employee id: ")
			st_temp  = list(filter(lambda a: a.gender == gender,employees))
			st_temp[0].set_gender(input("Enter new gender: "))
		elif choi == 5:
			break
		else:
			print("Invalid choice")			
