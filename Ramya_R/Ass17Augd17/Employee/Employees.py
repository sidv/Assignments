

import org as o
import change_emp as c
import search_emp as s
import team as t

employees = {} #empty List
organization = {}
teams = {}



def add_employee():
	#Add employee
	serial_no = input("\tEnter serial No: ")
	if serial_no not in employees.keys():
		name = input("\tEnter name: ")
		age = int(input("\tEnter age: "))
		gender = input("\tEnter the Gender: ")
		place =  input("\tEnter place: ")
		salary = input("\tEnter salary: ")
		prev_company = input("\tEnter previous company: ")
		join_date = input("\tEnter join date: ")
		empid = input("\tEnter empid: ") 
		temp ={
			"name":name,
			"age":age,
			"gender":gender,
			"place":place,
			"salary":salary,
			"prev_company":prev_company,
			"join_date":join_date,
			"empid":empid
			}
		employees[serial_no] = temp
	else:
		print("\tSerial No already Taken")
def delete_employee():
	#Delete employee
	print(employees)
	serial_no = input("\tEnter serial no: ")
	if serial_no not in employees.keys():
		print("\tWrong serial No")
	else:
		del employees[serial_no]

		
def display_employee():
	#Display employee
	#print(employees)
	for serial,employee in employees.items():
		print(f"\t{serial} | {employee['name']} | {employee['age']} | {employee['gender']} | {employee['place']}| {employee['salary']} | {employee['prev_company']} | {employee['join_date']} | {employee['empid']}")



