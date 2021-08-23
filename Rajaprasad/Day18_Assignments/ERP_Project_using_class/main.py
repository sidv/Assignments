from employee import Emp
from change_employee import *
from search_employee import *

emp = []  # empty list


def main_menu():
    print("1. Add employee")
    print("2. Delete employee")
    print("3. Search employee")
    print("4. Display all employee")
    print("5. Change a employee's data")
    print("6. exit")


def add_employee():
    emp_id = input("\tEnter employee id : ")
    name = input("\tEnter employee name : ")
    age = input("\tEnter employee's age : ")
    gender = input("\tEnter employee's gender : ")
    place = input("\tEnter employee's place : ")
    salary = input("\tEnter employee's salary : ")
    previous_company = input("\tEnter employee's previous company name : ")
    joining_date = input("\tEnter employee's joining date : ")

    emp_temp = Emp(emp_id, name, age, gender, place,
                   salary, previous_company, joining_date)
    emp.append(emp_temp)


def delete_employee():
    id = input("Enter employee id : ")
    for i in emp:
        if i.emp_id == id:
            emp.pop(emp.index(i))


def display_employee():
    name = input("Enter employee name : ")
    x = list(filter(lambda a: a.name == name, emp))
    if not x:
        print("Employee not found")
    else:
        for i in emp:
            i.display()


def search_employee():

    while True:
        search_employee_menu()
        ch = int(input("Enter choice : "))
        if ch == 1:
            serach_by_name()
        elif ch == 2:
            search_by_age()
        elif ch == 3:
            search_by_salary()
        elif ch == 4:
            search_by_gender()
        elif ch == 5:
            break


def change_emp_data():
    while True:
        change_emp_menu()
        ch = int(input("Enter choice : "))
        if ch == 1:
            modify_name()
        elif ch == 2:
            modify_age()
        elif ch == 3:
            modify_gender()
        elif ch == 4:
            modify_salary()
        elif ch == 5:
            break
        else:
            print("Invalid option")


while True:
    main_menu()
    ch = int(input("Enter choice : "))
    if ch == 1:
        # add employee
        add_employee()

    elif ch == 2:
        # delete employee
        delete_employee()

    elif ch == 3:
        # search employee
        search_employee()
    elif ch == 4:
        display_employee()
    elif ch == 5:
        change_emp_data()
    elif ch == 6:
        break
    else:
        print("Invalid option")
