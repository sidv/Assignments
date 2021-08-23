from employee import Employee

emp = []

def main_menu():
    print("\t1.Add Employee")
    print("\t2.Display Employee")
    print("\t3.exit")

while True:
    main_menu()
    ch = int(input("Enter choice : "))
    if ch == 1:
        # add employee
        emp.append(Employee())
        emp[-1].insert()
    elif ch == 2:
        # display employee
        for i in emp:
            i.display()
    elif ch == 3:
        break
    else:
        print("Invalid")
