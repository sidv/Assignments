print('storing and retriving employee information')
emp={}
emp['name'] = input('Enter employee name : ')
emp['age'] = int(input('Enter age : '))
emp['gender'] = input('Enter the gender of employee : ')
emp['place'] = input('Enter the place : ')
emp['salary'] = int(input('Enter salary :'))
emp['previous_company'] = input('Enter previous company name : ')

print('showing employee information:')
print(emp)