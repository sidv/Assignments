#2.Write a code to store employee information in dictionary(Only one employee details)
#Take input from user
#Properties: Name,Age,Gender,Place,Salary,Previous_company

employee = {}

emp_name  = input("Enter name")
emp_age = int(input("Enter age"))
emp_gender = input("Gender")
emp_place = input("Enter place")
emp_sal = input ("Enter salary")
emp_prevcomp = input("Enter previous company")

employee = {
		"emp_name" : emp_name,
		"emp_age" : emp_age,
		"emp_gender" : emp_gender,
		"emp_place" : emp_place,
		"emp_sal" : emp_sal,
		"emp_prevcomp" : emp_prevcomp
	   }
print("_____Employee Details_______")
print(employee)
