import json
import requests as req
ADD_EMPLOYEE_URL = "https://sidnodeapp.herokuapp.com/register"
DELETE_EMPLOYEE_URL = "https://sidnodeapp.herokuapp.com//delete"
SEARCH_EMPLOYEE_BY_NAME_URL ="https://sidnodeapp.herokuapp.com/getuserbyname"
SEARCH_EMPLOYEE_BY_ID_URL ="https://sidnodeapp.herokuapp.com/getuserbyid"
DISPLAY_EMPLOYEE_URL = "https://sidnodeapp.herokuapp.com/getalluser"
UPDATE_EMPLOYEE_USERNAME_URL = "https://sidnodeapp.herokuapp.com/changeusername"
UPDATE_EMPLOYEE_EMAIL_URL ="https://sidnodeapp.herokuapp.com/changeemail"



def add_employee():
	i = input("\tEnter employeeid")
	n = input("\tEnter name: ")
	u = input("\tEnter username: ")
	e = input("\tEnter email: ")
	s = input("\tEnter salary: ")
	p = input("\tEnter previous_company : ")
	payload = {"employee_id":i,"name": n,"username":u,"email":e,"salary":s,"previous_company":p}
	header = {"Content-Type": "application/json"}
	res = req.post(ADD_EMPLOYEE_URL, data=json.dumps(payload), headers = header)
	print(res.text)
	
def delete_employee():
	employee_id = input("\tEnter employee id to delete : ")
	d = {"employee_id":employee_id}
	header = {"Content-Type": "application/json"}
	res = req.post(DELETE_EMPLOYEE_URL, data=json.dumps(d), headers = header)
	print(res.text)
def search_employee_by_name():
	name = input("\tEnter name: ")
	d = {"name":name}
	header = {"Content-Type": "application/json"}
	res = req.post(SEARCH_EMPLOYEE_BY_NAME_URL, data=json.dumps(d), headers = header)
	print(res.json)
def search_employee_by_id():
	employee_id = input("\tEnter employeeid: ")
	d = {"employee_id":employee_id}
	header = {"Content-Type": "application/json"}
	res = req.post(SEARCH_EMPLOYEE_BY_ID_URL, data=json.dumps(d), headers = header)
	print(res.json)


def display_employee():
      
       
        res = req.get(DISPLAY_EMPLOYEE_URL)
        print(res.json())
        
def update_employee_username():
	employee_id=input("Enter the employee id to update")
	new_username = input("\tEnternew username: ")
	d = {"employee_id":employee_id,"username":new_username}
	header = {"Content-Type": "application/json"}
	res = req.put(UPDATE_EMPLOYEE_USERNAME_URL, data=json.dumps(d), headers = header)
	print(res.text)
   
def update_employee_email():
	employee_id = input("\tEnter employee id to update : ")
	new_email=input("\tEnter new email : ")
	d = {"employee_id":employee_id,"email":new_email}
	header = {"Content-Type": "application/json"}
	res = req.put(UPDATE_EMPLOYEE_EMAIL_URL, data=json.dumps(d), headers = header)
	print(res.text)


operations = {
	"1":add_employee,
	"2":delete_employee,
	"3":search_employee_by_name,
	"4":search_employee_by_id,
	"5":display_employee,
	"6":update_employee_username,
	"7":update_employee_email,
}


def main_menu():
	print("1.Add employee")
	print("2.Delete delete")
	print("3.search employee by name")
	print("4.search employee by id")
	print("5.Display employee")
	print("6.update_employee_usename")
	print("7.update_employee_email")


while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
