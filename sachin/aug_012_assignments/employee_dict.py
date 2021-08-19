"""2.Write a code to store employee information in dictionary(Only one employee details)
Take input from user
Properties: Name,Age,Gender,Place,Salary,Previous_company"""


employee = {} 

		

name = input("Enter name : ")
age = int(input("Enter Age : "))
gender = input("Enter Gender : ")
place = input("Enter the Place : ")
salary = int(input("Enter Salary : "))
previous_company = input("Enter Previous_company : ")
employee ={
    "Name":name,
    "Age":age,
    "Gender":gender,
    "Place":place,
    "Salary":salary,
    "Previous_company":previous_company
    }
print(employee)


