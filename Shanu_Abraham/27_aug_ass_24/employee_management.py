#Write a menu drievn code to for Employee management.
#	-Add employee(https://sidnodeapp.herokuapp.com/register)(POST)(Response TEXT)
#	-Delete employee(https://sidnodeapp.herokuapp.com//delete)(POST)(Response TEXT)
#	-Search employee by name(https://sidnodeapp.herokuapp.com/getuserbyname))(POST)(Response JSON)
#	-Search employee by id(https://sidnodeapp.herokuapp.com/getuserbyid)(POST)(Response JSON)
#	-display employee(https://sidnodeapp.herokuapp.com/getalluser)(GET)(Response JSON)
#	-update employee username(https://sidnodeapp.herokuapp.com/changeusername)(PUT)(Response TEXT)
#	-update employee email(https://sidnodeapp.herokuapp.com/changeemail)(PUT)(Response TEXT)
#Notes:Update operation must be by id
#Content Type : json
#Properties: id,name,username,email,salary,previous_company

import json
import requests as req

ADD_EMPLOYEE_URL = "https://sidnodeapp.herokuapp.com/register"
DELETE_EMPLOYEE_URL = "https://sidnodeapp.herokuapp.com//delete"
SEARCH_EMPLOYEE_NAME_URL = "https://sidnodeapp.herokuapp.com/getuserbyname"
SEARCH_EMPLOYEE_ID_URL = "https://sidnodeapp.herokuapp.com/getuserbyid"
DISPLAY_EMPLOYEE_URL = "https://sidnodeapp.herokuapp.com/getalluser"
UPDATE_EMPLOYEE_USERNAME_URL = "https://sidnodeapp.herokuapp.com/changeusername"
UPDATE_EMPLOYEE_EMAIL_URL = "https://sidnodeapp.herokuapp.com/changeemail"

def add_employee():
	emp_id = input("\tEnter employee id")
	name = input("\tEnter name:")
	username = input("\tEnter username")
	email = input("\tEnter email:")
	salary = input("\tEnter the salary")
	prv_com = input("\tEnter the previous company")
	payload = {"emp_id":emp_id,"name":name,"username":username,"email":email,"salary":salary,"prv_com":prv_com}
	header = {"Content-Type":"application/json"}
	res = req.post(ADD_EMPLOYEE_URL,data=json.dumps(payload),headers = header)
	print(res.text)

def delete_employee():
	emp_id = input("\tEnter employee id:")
	d = {"emp_id":emp_id}
	header = {"Content-Type":"application/json"}
	res = req.post(DELETE_EMPLOYEE_URL,data=json.dumps(d),headers = header)
	print(res.text)

def display_employee():
	#emp_id = input("\tEnter employee id:")
	#d = {"emp_id":emp_id}
	header = {"Content-Type":"application/json"}
	res = req.get(DISPLAY_EMPLOYEE_URL,headers = header)
	print(res.json())


def search_employee_id():
	emp_id = input("\tEnter employee id:")
	d = {"emp_id":emp_id}
	header = {"Content-Type":"application/json"}
	res = req.post(SEARCH_EMPLOYEE_ID_URL,data = json.dumps(d),headers = header)
	print(res.json())

def search_employee_name():
        name = input("\tEnter employee name:")
        d = {"name":name}
        header = {"Content-Type":"application/json"}
        res = req.post(SEARCH_EMPLOYEE_NAME_URL,data = json.dumps(d),headers = header)
        print(res.json())

def update_employee_username():
        username = input("\tEnter username:")
        d = {"username":username}
        header = {"Content-Type":"application/json"}
        res = req.post(DISPLAY_USER_URL,data = json.dumps(d),headers = header)
        print(res.text)

def update_employee_email():
        email = input("\tEnter email:")
        d = {"email":email}
        header = {"Content-Type":"application/json"}
        res = req.post(UPDATE_EMPLOYEE_EMAIL_URL,data = json.dumps(d),headers = header)
        print(res.text)

operations = {
	"1":add_employee,
	"2":delete_employee,
	"3":search_employee_id,
	"4":search_employee_name,
	"5":display_employee,
	"6":update_employee_username,
	"7":update_employee_email,
	
}


def main_menu():
	print("1.Add employee")
	print("2.Delete employee")
	print("3.search employee id")
	print("4.search employee name")
	print("5.Display employee")
	print("6.update employee username")
	print("7.update employee email")


while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()

