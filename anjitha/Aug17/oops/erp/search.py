from emp_store import employees

def search_menu():
	print("1. Search by name")
	print("2. Search by age")
	print("3. Search by salary")
	print("4. Search by gender")
	print("5. exit")
	
def search_main():	
	while True:
		search_menu()
		cho = int(input("Enter your choice"))
		if cho == 1:
			name = input("Enter name :")
			st = list(filter(lambda a: a.name == name , employees))
			if len(st) == 0: 
				print("No employee found")
			else:
				for i in st:
					print(f"{i.name}")
					print("We found")
		elif cho == 2:
			age = input("Enter age :")
			st = list(filter(lambda a: a.age == age , employees))
			if len(st) == 0:
				print("No employee found")
			else:
				for i in st:
					print(f"{i.age}")
					print("We found")
					
		elif cho == 3:
			salary = input("Enter salary :")
			st = list(filter(lambda a: a.salary == salary , employees))
			if len(st) == 0:
				print("No employee found")
			else:
				for i in st:
					print(f"{i.salary}")
					print("We found")
					
		elif cho == 4:
			gender = input("Enter gender :")
			st = list(filter(lambda a: a.gender == gender , employees))
			if len(st) == 0:
				print("No employee found")
			else:
				for i in st:
					print(f"{i.gender}")
					print("We found")
					
		elif cho == 5:
			break
		else:
			print("Invalid choice")






