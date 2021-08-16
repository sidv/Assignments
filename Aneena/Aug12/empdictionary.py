#Write a code to store employee information in dictionary(Only one employee details)
#Take input from user
#Properties: Name,Age,Gender,Place,Salary,Previous_company
employee = {}
while True:

	print("1.Add employee details")
	name=input("Enter the employee name\n")
	age=int(input("enter the age"))
	gender=input("enter the gender")
	place=input("Enter the place")
	salary=int(input("Enter the salary"))
	previous_company=input("Enter the previous company")
	employee =  {
		"name" : name,
		"age" : age,
		"gender" : gender,
		"place" : place,
		"salary" : salary,
		"previous_company" : previous_company
		}
	print(employee)
	break;	
