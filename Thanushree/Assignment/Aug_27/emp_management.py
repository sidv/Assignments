import json
import requests as req

ADD_EMP_URL = "https://sidnodeapp.herokuapp.com/register"
DELETE_EMP_URL = "https://sidnodeapp.herokuapp.com//delete"
SEARCH_EMP_BY_NAME_URL = "https://sidnodeapp.herokuapp.com/getuserbyname"
SEARCH_EMP_BY_ID_URL = "https://sidnodeapp.herokuapp.com/getuserbyid"
DISPLAY_EMP_URL = "https://sidnodeapp.herokuapp.com/getalluser"
UPDATE_EMP_UNAME_URL = "https://sidnodeapp.herokuapp.com/changeusername"
UPDATE_EMP_EMAIL_URL = "https://sidnodeapp.herokuapp.com/changeemail"

def add_emp():
	i = int(input("\tEnter id: "))
	n = input("\tEnter name: ")
	e = input("\tEnter email: ")
	u = input("\tEnter username: ")
	s = int(input("\tEnter salary : "))
	p = input("\tEnter previous company: ")
	payload = {"id":i,"name": n,"username":u,"email":e,"salary":s,"prev_comp":p}
	header = {"Content-Type": "application/json"}
	res = req.post(ADD_EMP_URL, data=json.dumps(payload), headers = header)
	print(res.text)

def delete_emp():
	id = int(input("\tEnter id: "))
	d = {"id":id}
	header = {"Content-Type": "application/json"}
	res = req.post(DELETE_EMP_URL, data=json.dumps(d), headers = header)
	print(res.text)

def search_emp_name():
	name = input("\tEnter the name of the employee to search")
	s_n = {"name":name}
	header = {"Content-Type": "application/json"}
	res = req.post(SEARCH_EMP_BY_NAME_URL,data=json.dumps(s_n), headers = header)
	print(res.json())

def search_emp_id():
	id = int(input("\tEnter id of the employee to search"))
	s_i = {"id":id}
	header = {"Content-Type": "application/json"}
	res = req.post(SEARCH_EMP_BY_ID_URL,data=json.dumps(s_i), headers = header)
	print(res.json())

def display_emp():
        name = input("\tEnter name: ")
        d = {"name":name}
        header = {"Content-Type": "application/json"}
        res = req.get(DISPLAY_EMP_URL, data=json.dumps(d), headers = header)
        print(res.json())

def update_emp_uname():
#	uname = input("\tEnter new username")
#	d = {"id":uname}
	d = {"id": input("enter emp id whose username you want to change: "),
        	"uname":input("Enter new username:")}
	header = {"Content-Type":"application.json"}
	res = req.put(UPDATE_EMP_UNAME_URL, data=json.dumps(d), headers = header)
	print(res.text)

def update_emp_email():
#	email = input("\Enter new email")
#	d = {"id":email}
	d = {"id": input("enter emp id whose email you want to change: "),
        	"email":input("Enter new email:")}
	header = {"Content-Type":"application.json"}
	res = req.put(UPDATE_EMP_EMAIL_URL, data = json.dumps(d),headers = header)
	print(res.text)

operations = {
	"1":add_emp,
	"2":delete_emp,
	"3":search_emp_name,
	"4":search_emp_id,
	"5":display_emp,
	"6":update_emp_uname,
	"7":update_emp_email
}


def main_menu():
	print("1.Add employee")
	print("2.Delete employee")
	print("3.Search employee by name")
	print("4.Search employee by id")
	print("5.Display employees")
	print("6.Update employee username")
	print("7.Update employee email")

while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
