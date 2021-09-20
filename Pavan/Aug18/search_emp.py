from emp_class import Employee 
from emp_store import employees

def search_employee():
	name = input("\tEnter name")
	found = False
	
	for i in employees:
		if i.name == name: 
			print(f"\t{i.name} | {i.age} | {i.gender} | {i.place} | {i.salary}| {i.previous_company} | {i.joining_date}")
			found = True
			break
	if found == False :
		print("\tNot found")

