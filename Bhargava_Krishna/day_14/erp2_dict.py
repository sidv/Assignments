def employee_menu():
    print("\nPress 1 for Add Employee  ")
    print("Press 2 for Delete Employee  ")
    print("Press 3 for Search Employee  ")
    print("Press 4 for Change Employee Data  ")
    print("Press 5 for Display  ")
    print("Press 6 for exit  ")
    print("\n_______________________________________________\n")

def add_employee():
    serial = int(input("Enter the serial number "))
    if serial not in emp.keys():
        name = input("Enter Employee name ")
        gender = input("Enter Employee gender ")
        age = int(input("Enter Employee age "))
        place = input("Enter Employee place ")
        slry = input("Enter salary ")
        pcmpny = input("Enter Previous Company name ")
        date = input("Enter joining date ")
        temp = {
            "name":name,
            "age":age,
            "gender":gender,
            "place":place,
            "slry":slry,
            "pcmpny":pcmpny,
            "date":date,
        }
        emp[serial] = temp
    else:
        print("serial No is already taken")

def delete_employee():
    serial = int(input("Enter serial no "))
    if serial not in emp.keys():
        print("invalid serial number")
    else:
        del emp[serial]

def search_employee():
    name = input("Enter employee name")
    found  = False
    for val in emp.values():
        if (val['name'] == name):
            found = True
            print(f"{val['name']} | {val['age']} | {val['place']} ")
    if(found == False):
        print("not found")


def change_menu():
    print("\nPress 1 for change name ")
    print("Press 2 for change age ")
    print("Press 3 for change gender ")
    print("Press 4 for change salary \n")

def change_name():
    newname = input("Enter new name for the employee ")
    emp[serial]['name'] = newname
def change_age():
    newage = int(input("Enter the new age "))
    emp[serial]['age'] = newage
def change_gender():
    newgender = input("Enter gender ")
    emp[serial]['gender'] = newgender
def change_salary():
    newsal = input("Enter new salary ")
    emp[serial]['slry'] = newsal


def display_employee():
    for serial,empl in emp.items():
        print(f"{serial} | {empl['name']} | {empl['age']} | {empl['place']} | {empl['slry']} | {empl['date']} | {empl['gender']}  | {empl['pcmpny']} ")

emp = {}
while True:

    employee_menu()
    ch = int(input("Enter your choice  "))
    print("")
    if (ch == 1):
        add_employee()
    elif (ch == 2):
        delete_employee()
    elif (ch == 3):
        search_employee()
    elif (ch == 4):
        serial = int(input("Enter serial no "))
        if serial not in emp.keys():
            print("Invalid serial no")
        else:
            change_menu()
            cho = int(input("Enter an option"))
            if (cho == 1):
                change_name()
            elif (cho == 2):
                change_age()
            elif (cho == 3):
                change_gender()
            elif (cho == 4):
                change_salary()
            else:
                print("invalid choice")

    elif (ch == 5):
           display_employee()
    elif (ch == 6):
        break
    else:
        print("invalid choice ")
