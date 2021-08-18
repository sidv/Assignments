from employee import Emp

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
    name = input("Enter name :")
    emp_l = list(filter(lambda a: a.name == name, emp))
    if len(emp) == 0:  # not st #st
        print("No employee found")
    else:
        pass


def search_employee_menu():
    print("\t1.search by name ")
    print("\t2.search by age ")
    print("\t3.search by salary ")
    print("\t4.search by gender ")
    print("\t5.exit ")


def serach_by_name():
    name = input("Enter name :")
    emp_l = list(filter(lambda a: a.name == name, emp))
    if len(emp) == 0:  # not st #st
        print("No employee found")
    else:
        for i in emp:
            print(
                f'{i.name} |{i.age} | {i.gender}|{i.place} |{i.salary} | {i.previous_company} | {i.joining_date} ')


def search_by_age():
    age = input("Enter age :")
    emp_l = list(filter(lambda a: a.age == age, emp))
    if len(emp) == 0:  # not st #st
        print("No employee found")
    else:
        for i in emp:
            print(
                f'{i.name} |{i.age} | {i.gender}|{i.place} |{i.salary} | {i.previous_company} | {i.joining_date} ')


def search_by_salary():
    salary = input("Enter salary :")
    emp_l = list(filter(lambda a: a.salary == salary, emp))
    if len(emp) == 0:  # not st #st
        print("No employee found")
    else:
        for i in emp:
            print(
                f'{i.name} |{i.age} | {i.gender}|{i.place} |{i.salary} | {i.previous_company} | {i.joining_date} ')


def search_by_gender():
    gender = input("Enter gender :")
    emp_l = list(filter(lambda a: a.gender == gender, emp))
    if len(emp) == 0:  # not st #st
        print("No employee found")
    else:
        for i in emp:
            print(
                f'{i.name} |{i.age} | {i.gender}|{i.place} |{i.salary} | {i.previous_company} | {i.joining_date} ')


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


def display_employee():
    for i in emp:
        print(
            f'{i.name} |{i.age} | {i.gender}|{i.place} |{i.salary} | {i.previous_company} | {i.joining_date} ')


def change_emp_data():
    pass


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
