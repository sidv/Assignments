#write a code to store employee information in dictionary
employee={}
while True:
	print("add employee info")
	name=input("enter the  employee name")
	age=int(input("ente the employee age"))
	genter=input("enter the genter")
	place=input("enter the place")
	salary=int(input("enter salary"))
	previous_company=("enter previous_company")
	employee = {
		"name":name,
		"age":age,
		"genter":genter,
		"place":place,
		"salary":salary,
		"previous_company":previous_company,
		}
	print(employee)
	break;
