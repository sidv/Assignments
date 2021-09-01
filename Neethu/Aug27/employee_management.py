import json
import requests as req
ADD_USER_URL = "https://sidnodeapp.herokuapp.com/register"
DELETE_USER_URL = "https://sidnodeapp.herokuapp.com//delete"
DISPLAY_USER_URL = "https://sidnodeapp.herokuapp.com/getalluser"
SEARCH_EMP_BY_ID = "https://sidnodeapp.herokuapp.com/getuserbyid"
SEARCH_EMP_BY_NAME = "https://sidnodeapp.herokuapp.com/getuserbyname"
UPDATE_EMP_UNAME = "https://sidnodeapp.herokuapp.com/changeusername"
UPDATE_EMP_EMAIL = "https://sidnodeapp.herokuapp.com/changeemail"

def add_employee():
	u_id = int(input("\t Enter the id : "))
	name = input("\t Enter name : ")
	u_name = input("\t Enter the user name : ")
	email = input("\t Enter email : ")
	sal = int(input("\t Enter the salary : "))
	prev_cmp = input("\t Entere the previous company : ")
	 
	payload = {"id":u_id,"name":name,"username":u_name,"email":email,"salary":sal,"previous_company":prev_cmp}
	header = {"Content-Type": "application/json"}
	res = req.post(ADD_USER_URL, data=json.dumps(payload), headers = header)
	print(res.text)


#id,name,username,email,salary,previous_company

def delete_employee():
	u_id = input("\t Enter the id : ")
	d = {"id":u_id}
	header = {"Content-Type": "application/json"}
	res = req.post(DELETE_USER_URL, data=json.dumps(d), headers = header)
	print(res.text)

def display_employee():
#	u_id = input("\t Enter the id : ")
#	d = {"id":u_id}
	header = {"Content-Type": "application/json"}
	res = req.get(DISPLAY_USER_URL, headers = header)
	print(res.json())
        
def search_emp_by_id(): 
	u_id = int(input("\t Enter the employee id : "))
	d = {"id":u_id}
	header = {"Content-Type": "application/json"}
	res = req.post(DISPLAY_USER_URL, data=json.dumps(d), headers = header)
	print(res.json())    
        
def search_emp_by_name():
	name = input("\t Enter the employee name : ")
	name = {"name":name}
	header = {"Content-Type": "application/json"}
	res = req.post(DISPLAY_USER_URL, data=json.dumps(d), headers = header)
	print(res.json())

def update_emp_uname():
	payload = {
	"id": input("\t Enter user_id whose username you want to change : "),
	"username":input("\t Enter new username : ")
	}
	header = {"Content-Type": "application/json"}

	res = req.put(UPDATE_EMP_UNAME,data=json.dumps(payload),headers = header)
	print(res.text)
	

def update_emp_email():
	payload = {
	"id": input("Enter user_id whose email you want to change : "),
	"email":input("Enter new email : ")
	}
	header = {"Content-Type": "application/json"}

	res = req.put(UPDATE_EMP_EMAIL,data=json.dumps(payload),headers = header)
	print(res.text)
		

operations = {
	"1":add_employee,
	"2":delete_employee,
	"3":search_emp_by_id,
	"4":search_emp_by_name,
	"5":display_employee,
	"6":update_emp_uname,
	"7":update_emp_email
}


def main_menu():
	print("1.Add employee")
	print("2.Delete Employee")
	print("3.Search Employee by ID")
	print("4.Search Employee by Name")
	print("5.Display Employee")
	print("6.Upadte Employee Username")
	print("7.Upadte Employee Email")


while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
