from user import *

emp = []


def menu():
    print("\t1.Add Employee")
    print("\t2.Display Employee")
    print("\t3.exit")


while True:
    menu()
    ch = int(input("Enter choice : "))
    if ch == 1:
        emp.append(Employee())
        emp[-1].insert()
    elif ch == 2:
        for i in emp:
            i.display() 
    elif ch == 3:
        break
    else:
        print("Invalid")
