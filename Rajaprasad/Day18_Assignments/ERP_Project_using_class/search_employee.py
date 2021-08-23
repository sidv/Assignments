

def search_employee_menu():
    print("\t1.search by name ")
    print("\t2.search by age ")
    print("\t3.search by salary ")
    print("\t4.search by gender ")
    print("\t5.exit ")


def serach_by_name():
    name = input("Enter name :")
    if not list(filter(lambda a: a.name == name, emp)):
        print("No employee found")
    else:
        for i in emp:
            print(
                f'{i.name} |{i.age} | {i.gender}|{i.place} |{i.salary} | {i.previous_company} | {i.joining_date} ')


def search_by_age():
    age = input("Enter age :")
    if not list(filter(lambda a: a.age == age, emp)):
        print("No employee found")
    else:
        for i in emp:
            print(
                f'{i.name} |{i.age} | {i.gender}|{i.place} |{i.salary} | {i.previous_company} | {i.joining_date} ')


def search_by_salary():
    salary = input("Enter salary :")
    if not list(filter(lambda a: a.salary == salary, emp)):
        print("No employee found")
    else:
        for i in emp:
            print(
                f'{i.name} |{i.age} | {i.gender}|{i.place} |{i.salary} | {i.previous_company} | {i.joining_date} ')


def search_by_gender():
    gender = input("Enter gender :")
    if not list(filter(lambda a: a.gender == gender, emp)):
        print("No employee found")
    else:
        for i in emp:
            print(
                f'{i.name} |{i.age} | {i.gender}|{i.place} |{i.salary} | {i.previous_company} | {i.joining_date} ')
