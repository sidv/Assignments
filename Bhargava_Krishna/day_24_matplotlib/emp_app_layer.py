import json
import requests as rq
ADD_EMP_URL = "https://sidnodeapp.herokuapp.com/register"
DELETE_EMP_URL = "https://sidnodeapp.herokuapp.com//delete"
SEARCH_BY_NAME = "https://sidnodeapp.herokuapp.com/getuserbyname"
SEARCH_BY_ID = "https://sidnodeapp.herokuapp.com/getuserbyid"
DISPLAY = "https://sidnodeapp.herokuapp.com/getalluser"
UPDATE = "https://sidnodeapp.herokuapp.com/changeusername"
UPDATE_MAIL = "https://sidnodeapp.herokuapp.com/changeemail"

def add_emp():
	emp_id = int(input("\t\tEnter employee id: "))
	name = input("\t\tEnter name ")
	username = input("\t\tEnter username ") 
	email = input("\t\tEnter mail id ")
	salary = input("\t\tEnter salary ")
	pre_cmp = input("\t\tEnter previous company ")
	pl = { "id" : emp_id, "name" : name, "username" : username, "email" : email, "salary" : salary, "previos_company" : pre_cmp}
	hd = {"Content-Type": "application/json"}
	res = rq.post(ADD_EMP_URL, data=json.dumps(pl), headers = hd)
	print(res.text)
	
def delete_emp():
	id1 = int(input("\t\tEnter employee id to delete : "))
	d = {"id" : id1}
	h = {"Content-Type": "application/json"}
	res = rq.post(DELETE_EMP_URL, data = json.dumps(d), headers = h)
	print(res.text)
	
def search_by_name():
	name = input("\t\tEnter name ")
	payn = {"name" : name}
	hdr = {"Content-Type": "application/json"}
	res = rq.post(SEARCH_BY_NAME, data = json.dumps(payn), headers = hdr)
	print(res.json())
	
def search_by_id():
	eid = int(input("\t\tEnter id "))
	payid = {"id" : eid}
	hdr = {"Content-Type": "application/json"}
	res = rq.post(SEARCH_BY_ID, data = json.dumps(payid), headers = hdr)
	print(res.json())
	
def display_emp():
	name = input("\t\tEnter name ")
	payd = {"name" : name }
	hd = {"Content-Type": "application/json"}
	res = rq.get(DISPLAY, data = json.dumps(payd), headers = hd)
	print(res.json())
	
def update_username():
	id2 = int(input("\tEnter id: "))
	name = input("\tEnter name to change ")
	payload = {"id" : id2 , "username" : name}
	header = {"Content-Type": "application/json"}
	res = rq.put(UPDATE, data = json.dumps(payload), headers = header)
	print(res.text)
	
def update_email():
	id3 = int(input("\t\tEnter id: "))
	mail = input("\t\tEnter mail to change ")
	pd = {"id" : id3, "email" : mail}
	hd = {"Content-Type": "application/json"}
	res = rq.put(UPDATE_MAIL, data = json.dumps(pd), headers = hd)
	print(res.text)
	
	
	

def main_menu():
	print("\t1.Add employee")
	print("\t2.Delete employee")
	print("\t3.Search employee by name")
	print("\t4.Search employee by id")
	print("\t5.Display employee")
	print("\t6.Update employee username")
	print("\t7.Update employee mail")
	
operations = {
		1 : add_emp,
		2 : delete_emp,
		3 : search_by_name,
		4 : search_by_id,
		5 : display_emp,
		6 : update_username,
		7 : update_email
}		

		
	
while True:
	main_menu()
	ch = int(input("\tEnter your choice "))
	
	operations[ch]()
