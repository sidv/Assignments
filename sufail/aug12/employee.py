print("To add employee details in dictionary")

employee={}

print("enter details")
name=input("name=")
age=int(input("age="))
gender=input("gender =")
place=input("place=")
salary=int(input("salary="))
pcompany=input("previous company")
employee= {
		"Name":name,
		"Rate":age,
		"Gender":gender,
		"Place":place,
		"Salary":salary,
		"Previous_company":pcompany
	  }
print(employee)

