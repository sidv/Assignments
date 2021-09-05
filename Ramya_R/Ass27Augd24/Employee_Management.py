import json
import requests as req
ADD_USER_URL = "https://sidnodeapp.herokuapp.com/register"
DELETE_USER_URL = "https://sidnodeapp.herokuapp.com/delete"
DISPLAY_USER_URL = "https://sidnodeapp.herokuapp.com/getalluser"
SEARCH_BY_NAME_URL = "https://sidnodeapp.herokuapp.com/getuserbyname"
SEARCH_BY_ID = "https://sidnodeapp.herokuapp.com/getuserbyid"
UPDATE_EMP_USERNAME_URL = "https://sidnodeapp.herokuapp.com/changeusername"
UPDATE_EMP_EMAIL_URL = "https://sidnodeapp.herokuapp.com/changeemail"


def add_employee():
	id = input("\tEnter emplyee id: ")
	name = input("\tEnter name: ")
	email = input("\tEnter email: ")
	username = input("\tEnter username: ")
	salary = int(input("\tEnter salary : "))
	pre_comp = input("\tEnter previous company : ")
	payload = {"id": id, "name": name, "email": email, "username": username, "salary": salary, "pre_comp": pre_comp}
	header = {"Content-Type": "application/json"}
	res = req.post(ADD_USER_URL, data=json.dumps(payload), headers=header)
	print(res.text)




def delete_employee():
	#name = input("\tEnter name: ")
	#d = {"name": name}
	id = input("Enter ID : ")
	d = {"id": id}
	header = {"Content-Type": "application/json"}
	res = req.post(DELETE_USER_URL, data=json.dumps(d), headers=header)
	print(res.text)


def display_all_employee():
	header = {"Content-Type": "application/json"}
	res = req.get(DISPLAY_USER_URL, headers=header)
	print(res.json())



def search_employee_by_id():
	id = input("Enter ID : ")
	payload = {"id": id}
	header = {"Content-type": "application/json"}
	res = req.post(SEARCH_BY_ID, data=json.dumps(payload), headers=header)
	print(res.json())




def search_emp_by_name():
	name = input("Enter name : ")
	payload = {"name": name}
	header = {"Content-type": "application/json"}
	res = req.post(SEARCH_BY_NAME_URL, data=json.dumps(payload), headers=header)
	print(res.json())



def update_employee_username():
	id = input("Enter ID : ")
	username = input("Enter username : ")
	payload = {"id": id, "username": username}
	header = {"Content-type": "application/json"}
	res = req.put(UPDATE_EMP_USERNAME_URL, data=json.dumps(payload), headers=header)
	print(res.text)


def update_employee_email():
	id = input("Enter ID: ")
	email = input("Enter email : ")
	payload = {"id": id, "email": email}
	header = {"Content-type": "application/json"}
	res = req.put(UPDATE_EMP_EMAIL_URL, data=json.dumps(payload), headers=header)
	print(res.text)


operations = {
	"1": add_employee,
	"2": delete_employee,
	"3": display_all_employee,
	"4": search_emp_by_name,
	"5": search_employee_by_id,
	"6": update_employee_username,
	"7": update_employee_email
}


def main_menu():
	print("1.Add employee")
	print("2.Delete employee")
	print("3.Display employee")
	print("4.search employee by name ")
	print("5.search employee by id")
	print("6.update employee username")
	print("7.update employee email ")


while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
