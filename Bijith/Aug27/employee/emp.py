import json
import requests as req
ADD_EMP_URL = "https://sidnodeapp.herokuapp.com/register"
DELETE_EMP_URL = "https://sidnodeapp.herokuapp.com//delete"
SEARCH_EMP_N_URL = "https://sidnodeapp.herokuapp.com/getuserbyname"
SEARCH_EMP_I_URL = "https://sidnodeapp.herokuapp.com/getuserbyid"
DISPLAY_EMP_D_URL = "https://sidnodeapp.herokuapp.com/getalluser"
UPDATE_EMP_U_URL = "https://sidnodeapp.herokuapp.com/changeusername"
UPDATE_EMP_E_URL = "https://sidnodeapp.herokuapp.com/changeemail"


def add_emp():
	i = int(input("\tEnter id: "))
	n = input("\tEnter name: ")
	u = input("\tEnter username: ")
	e = input("\tEnter email: ")
	s = int(input("\tEnter salary: "))
	p = input("\tEnter previous_company: ")
	payload = {"id": i,"name":n,"username":u,"email":e,"salary":s,"previous_company":p}
	header = {"Content-Type": "application/json"}
	res = req.post(ADD_EMP_URL, data=json.dumps(payload), headers = header)
	print(res.text)

def delete_emp():
	id = int(input("\tEnter id: "))
	d = {"id":id}
	header = {"Content-Type": "application/json"}
	res = req.post(DELETE_EMP_URL, data=json.dumps(d), headers = header)
	print(res.text)

def search_emp_by_name():
        name = input("\tEnter name: ")
        d = {"name":name}
        header = {"Content-Type": "application/json"}
        res = req.post(SEARCH_EMP_N_URL, data=json.dumps(d), headers = header)
        print(res.json())

def search_emp_by_id():
        id = int(input("\tEnter emp_by_id: "))
        d = {"id":id}
        header = {"Content-Type": "application/json"}
        res = req.post(SEARCH_EMP_I_URL, data=json.dumps(d), headers = header)
        print(res.json())
        
def display_emp():
        name = input("\tEnter name: ")
        d = {"name":name}
        header = {"Content-Type": "application/json"}
        res = req.get(DISPLAY_EMP_D_URL, data=json.dumps(d), headers = header)
        print(res.json())
        
def update_emp_username():
        payload = {"id": input("enter user_id whose username you want to change: "),
        	"username":input("Enter new username:")}    
        header = {"Content-Type": "application/json"}
        res = req.put(UPDATE_EMP_U_URL, data=json.dumps(payload), headers = header)
        print(res.text)    
def update_emp_email():
	payload = {"id": input("enter user_id whose EMAIL you want to change: "),
        	"email":input("Enter new email:")}    
	header = {"Content-Type": "application/json"}
	res = req.put(UPDATE_EMP_E_URL, data=json.dumps(payload), headers = header)
	print(res.text)
        
        
operations = {
	"1":add_emp,
	"2":delete_emp,
	"3":search_emp_by_name,
	"4":search_emp_by_id,
	"5":display_emp,
	"6":update_emp_username,
	"7":update_emp_email
}


def main_menu():
	print("1.Add employee")
	print("2.Delete employee")
	print("3.search employee by name")
	print("4.search employee by id")
	print("5.display employee")
	print("6.update employee username")
	print("7.update employee email")
	
	


while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
