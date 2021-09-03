employee = {}
 

name = input("Enter employee name:")
age = input("Enter age: ")
gender = input("Enter the gender: ")
place = input("Enter the place: ")
salary = input("Enter the salary: ")
previous_company = input("Enter the previous company: ")

employee["name"] = name
employee["age"] = age
employee["gender"] = gender
employee["place"] = place
employee["salary"] = salary
employee["previous_company"] = previous_company

for key, value in employee.items():
    print(f"{key}  :  {value}")
