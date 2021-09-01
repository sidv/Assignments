import json
import requests as req
ADD_EMPLOYEE = "https://sidnodeapp.herokuapp.com/register"
DELETE_EMPLOYEE = "https://sidnodeapp.herokuapp.com//delete"
SEARCH_EMPLOYEE_NAME = "https://sidnodeapp.herokuapp.com/getuserbyname"
SEARCH_EMPLOYEE_ID = "https://sidnodeapp.herokuapp.com/getuserbyid"
DISPLAY_EMPLOYEE = "https://sidnodeapp.herokuapp.com/getalluser"
UPDATE_EMPLOYEE_USERNAME = "https://sidnodeapp.herokuapp.com/changeusername"
UPDATE_EMPLOYEE_EMAIL = "https://sidnodeapp.herokuapp.com/changeemail"

def add_employee():

    payload = {
        "id":input("\tenter the id of employee :"),
        "name":input("\tenter the name of employee :"),
        "username":input("\tenter the username of employee :"),
        "email":input("\tenter the email of employee :"),
        "salary":input("\tenter the salary of employee :"),
        "previous_company":input("\tenter the previous company of employee :")
    }

    header = {"Content-Type": "application/json"}
    res = req.post(ADD_EMPLOYEE, data=json.dumps(payload), headers = header)
    print(res.text)

def delete_employee():
    payload = {  
        "id":input("\tenter the id of employee :")
    }

    header = {"Content-Type": "application/json"}
    res = req.post(DELETE_EMPLOYEE, data=json.dumps(payload), headers = header)
    print(res.text)


def Search_employee_by_name():
    payload = {
        "name":input("\tenter the id of employee :")
    }

    header = {"Content-Type": "application/json"}
    res = req.post(SEARCH_EMPLOYEE_NAME, data=json.dumps(payload), headers = header)
    print(res.json())

def Search_employee_by_id():
    payload = {
        "id":input("\tenter the id of employee :")
    }

    header = {"Content-Type": "application/json"}
    res = req.post(SEARCH_EMPLOYEE_ID, data=json.dumps(payload), headers = header)
    print(res.json())    

def display_employee(): 
    header = {"Content-Type": "application/json"}
    res = req.get(DISPLAY_EMPLOYEE, headers = header)
    print(res.json())

def update_employee_username():
    payload = {
        "username":input("\tenter the username of employee :"),
    }

    header = {"Content-Type": "application/json"}
    res = req.put(UPDATE_EMPLOYEE_USERNAME, data=json.dumps(payload), headers = header)
    print(res.text)

def update_employee_email():
    payload = {
        "email":input("\tenter the email of employee :")
    }

    header = {"Content-Type": "application/json"}
    res = req.put(UPDATE_EMPLOYEE_EMAIL, data=json.dumps(payload), headers = header)
    print(res.text)


operations = {
	"1":add_employee,
	"2":delete_employee,
	"3":Search_employee_by_name,
    "4":Search_employee_by_id,
    "5":display_employee,
    "6":update_employee_username,
    "7":update_employee_email
}


def main_menu():
    print("1.Add employee")
    print("2.Delete employee")
    print("3.Search employee by name")
    print("4.Search employee by id")
    print("5.display employee")
    print("6.update employee username")
    print("7.update employee email")
    


while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
