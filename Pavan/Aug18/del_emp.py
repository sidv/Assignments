from emp_class import Employee 
from emp_store import employees

def delete_employee():
	print(employees)
	eid=input("Enter the employye id:")
	for i in employees:
		if i.empid == eid:
			employees.pop(employees.index(i))

