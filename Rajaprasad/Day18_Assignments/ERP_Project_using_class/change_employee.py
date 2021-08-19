
def change_emp_menu():
    print("\t1.modify name of employee")
    print("\t2.modify age of employee")
    print("\t3.modify gender of employee")
    print("\t4.modify salary of employee")
    print("\t5.exit")


def modify_name():
    name = input("Enter employee name : ")
    x = list(filter(lambda a: a.name == name, emp))
    if not x:
        print("Employee not found")
    else:
        x[0].set_name(input("Enter new name : "))


def modify_age():
    age = input("Enter employee age : ")
    x = list(filter(lambda a: a.age == age, emp))
    if not x:
        print("Employee not found")
    else:
        x[0].set_age(input("Enter new age : "))


def modify_gender():
    gender = input("Enter employee gender : ")
    x = list(filter(lambda a: a.gender == gender, emp))
    if not x:
        print("Employee not found")
    else:
        x[0].set_gender(input("Enter new gender : "))


def modify_salary():
    salary = input("Enter employee salary : ")
    x = list(filter(lambda a: a.salary == salary, emp))
    if not x:
        print("Employee not found")
    else:
        x[0].set_salary(input("Enter new salary : "))
