import json
import requests as req
ADD_EMP = "https://sidnodeapp.herokuapp.com/register"
DL_EMP = "https://sidnodeapp.herokuapp.com/delete"
S_EMP_NM = "https://sidnodeapp.herokuapp.com/getuserbyname"
S_EMP_ID = "https://sidnodeapp.herokuapp.com/getuserbyid"
U_EMP_NM = "https://sidnodeapp.herokuapp.com/changeusername"
U_EMP_EM = "https://sidnodeapp.herokuapp.com/changeemail"
DISP_EMP = "https://sidnodeapp.herokuapp.com/getalluser"

def add():
    id = input("\t Enter ID: ")
    n = input("\tEnter name: ")
    e = input("\tEnter email: ")
    u = input("\tEnter username: ")
    s = input("\tEnter salary : ")
    cmp = input("\tEnter previous company")
    payload = {"id": id,"name": n,"username":u,"email":e,"salary":s,"previous_company":cmp}
    header = {"Content-Type": "application/json"}
    res = req.post(ADD_EMP, data=json.dumps(payload), headers = header)
    print(res.text)

def delete():
	id = input("\tEnter Id: ")
	d = {"id":id}
	header = {"Content-Type": "application/json"}
	res = req.post(DL_EMP, data=json.dumps(d), headers = header)
	print(res.text)

def search_name():
    name = input("\tEnter Name: ")
    d = {"name":name}
    header = {"Content-Type": "application/json"}
    res = req.post(S_EMP_NM, data=json.dumps(d), headers = header)
    print(res.json)

def search_id():
    id = input("\tEnter Id: ")
    d = {"id":id}
    header = {"Content-Type": "application/json"}
    res = req.post(S_EMP_ID, data=json.dumps(d), headers = header)
    print(res.json)

def update_uname():
    uname = input("\tEnter User name: ")
    d = {"username":uname}
    header = {"Content-Type": "application/json"}
    res = req.put(U_EMP_NM, data=json.dumps(d), headers = header)
    print(res.text)

def update_email():
    uemail = input("\tEnter Email: ")
    d = {"username":uemail}
    header = {"Content-Type": "application/json"}
    res = req.put(U_EMP_EM, data=json.dumps(d), headers = header)
    print(res.text)

def display():
        header = {"Content-Type": "application/json"}
        res = req.get(DISP_EMP, headers = header)
        print(res.json())

operations = {
	"1":add,
	"2":delete,
    "3":search_name,
    "4":search_id,
    "5":update_uname,
    "6":update_email,
	"7":display
}


def main_menu():
    print("1.Add Employee")
    print("2.Delete Employee")
    print("3.Serch by name")
    print("4.Search by id")
    print("5.update username")
    print("6.update email") 
    print("7.Display all users")


while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()