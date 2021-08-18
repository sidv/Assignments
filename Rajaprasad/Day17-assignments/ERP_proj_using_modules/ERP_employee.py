
emp = {}  # empty dictionary


def my_decorator(func):

    def wrap_func():
        print('*'*30)
        func()
        print('*'*30)

    return wrap_func


@my_decorator
def main_menu():
    print("1.Add Employee")
    print("2.Delete Employee")
    print("3.Search Employee")
    print("4.Change Employee Data")
    print("5.Display employee list")
    print("6.manage all groups")
    print("7.manage organisation")
    print("8.exit")


@my_decorator
def add_employee():
    # add employee
    serial_no = input('Enter serial no : ')
    emp[serial_no] = {
        'name': input("Enter employee name : "),
        'age': int(input('age : ')),
        'gender': input('gender : '),
        'salary': int(input('salary : ')),
        'previous_company': input('enter previous company name : '),
        'joining_date': input("Joining date : ")
    }
    print("!"*30)
    print('Employee added successful')


@my_decorator
def delete_employee():
    serial_no = input('Enter serial number: ')
    if serial_no not in emp.keys():
        print('please provide right serial number')
    else:
        del emp[serial_no]


@my_decorator
def serach_emp_by_name():
    name = input('Enter employee name for search : ')
    Flag = False
    print(list(filter(lambda a: a["name"] == name, emp.values())))
    Flag = True
    if Flag == False:
        print('employee not found')


@my_decorator
def serach_emp_by_age():
    age = int(input('Enter employee age for search : '))
    Flag = False
    print(list(filter(lambda a: a["age"] == age, emp.values())))
    Flag = True
    if Flag == False:
        print('employee not found')


@my_decorator
def serach_emp_by_gender():
    gender = input('Enter employee gender for search : ')
    Flag = False
    print(list(filter(lambda a: a["gender"] == gender, emp.values())))
    Flag = True
    if Flag == False:
        print('employee not found')


@my_decorator
def serach_emp_by_salary():
    salary = int(input('Enter employee salary for search : '))
    Flag = False
    print(list(filter(lambda a: a["salary"] == salary, emp.values())))
    Flag = True
    if Flag == False:
        print('employee not found')


@my_decorator
def search_emp_menu():
    print("\t1.search employee by name")
    print("\t2.search employee by age")
    print("\t3.search employee by gender")
    print("\t4.search employee by salary")
    print("\t5.exit")


@my_decorator
def search_employee():
    while True:
        search_emp_menu()
        ch = int(input("Enter choice : "))
        if ch == 1:
            serach_emp_by_name()
        elif ch == 2:
            serach_emp_by_age()
        elif ch == 3:
            serach_emp_by_gender()
        elif ch == 4:
            serach_emp_by_salary()
        elif ch == 5:
            break
        else:
            print("Invalid option ")


@my_decorator
def change_employee_data():
    serial_no = input('Enter serial number : ')
    if serial_no not in emp.keys():
        print('please provide right serial number !')
    else:
        print('modify employee data')
        print('a,A =>change employee name \nb,B => modify gender \nc,C => modify age \nd,D => modify salary ')
        choice = input('Enter option: ')
        if choice == 'a' or choice == 'A':
            emp[serial_no]['name'] = input('Enter new name : ')
        elif choice == 'b' or choice == 'B':
            emp[serial_no]['gender'] = input('new Gender :')
        elif choice == 'c' or choice == 'C':
            emp[serial_no]['age'] = int(input('enter new age : '))
        elif choice == 'd' or choice == 'D':
            emp[serial_no]['salary'] = int(input('enter updated salary : '))
        else:
            print('Invalid option ')


@my_decorator
def display_data():
    print('Displaying all employees data')
    for i, v in emp.items():
        print('-'*10)
        print(
            f' { i }| { v["name"]} | {v["age"]} | {v["gender"]} | {v["salary"]} | {v["previous_company"]}  | {v["joining_date"]} ')
        print('-'*10)
