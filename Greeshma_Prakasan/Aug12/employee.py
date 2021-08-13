Employee = {}

name = input("Enter the name of Employee : ")
age = int(input("Enter the age of Employee : "))
gen = input("Enter the gender of Employee : ")
place = input("Enter the place of Employee : ")
salary = int(input("Enter the salary of Employee : "))
pre = input("Enter the previous company of Employee : ")

Employee["Name"] = name
Employee["Age"] = age
Employee["Gender"] = gen
Employee["Place"] = place
Employee["Salary"] = salary
Employee["Previous_Company"] = pre

print(Employee)
