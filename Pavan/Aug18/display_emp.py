from emp_class import Employee 
from emp_store import employees

def display_employee():
	for i in employees:
		print(f"{i.name} | {i.age} | {i.gender} | {i.place} | {i.salary}| {i.previous_company} | {i.joining_date}")
