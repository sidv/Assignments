print("STORE EMPLOYEE INFO")

employee={}
serial_no = int(input("Enter serial No : "))
name = input("Enter name : ")
age = int(input("Enter age : "))
gender = input("Enter the gender : ")
place = input("Enter the place : ")
salary = input("Enter the salary : ")
prev_company = input("Enter the previous company : ")
temp ={
	"Emp_name":name,
	"Emp_age":age,
	"Emp_gender":gender,
	"Place":place,
	"Salary":salary,
	"Prev_company":prev_company
	}
employee[serial_no] = temp
print(employee)
