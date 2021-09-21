print(" " * 10, "ERP system")
emp = {}  # empty dictionary
group = {}  # empty dictionary
org = {}  # empty dictionary
# small decorator for displaying data


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


@my_decorator
def create_org():
    org_name = input("Enter organisation name : ")
    if org_name not in org.keys():
        org[org_name] = {}
        print(f"{org_name} organisation created successfully ")

    else:
        print(f"{org_name} organisation already available on system !")


@my_decorator
def modify_org_name():
    org_name = input("Enter organisation name : ")
    if org_name not in org.keys():
        print(f"{org_name} organisation not available on system !")
    else:
        temp = org[org_name]
        del org[org_name]
        org_name = input("Enter new organisation name : ")
        org[org_name] = temp
        print(f'{org_name} organisation name updated successfully ')


@my_decorator
def show_org():
    org_name = input("Enter organisation name : ")
    if org_name not in org.keys():
        print(f"{org_name} organisation not available on the system !")
    else:
        print(org)
        # for k, v in org[org_name].values():
        #     name_str = ""
        #     for i in v:
        #         name_str = name_str + "|" + i + emp[i]['name']
        #     print(f'{i} | {name_str}')


@my_decorator
def manage_org_menu():
    print("1.Add organistion")
    print("2.modify organistaion")
    print("3.show organisation")
    print("4.exit")


def manage_org():

    while True:
        manage_org_menu()
        ch = int(input("Enter choice : "))
        if ch == 1:
            # create organisation
            create_org()
        elif ch == 2:
            # modify organisation
            modify_org_name()
        elif ch == 3:
            # show organisation
            show_org()
        elif ch == 4:
            break
        else:
            print("Invalid option")


@my_decorator
def manage_all_group_menu():
    print("\t1.Create Group")
    print("\t2.Display Groups")
    print('\t3.rename group')
    print("\t4.Manage Group(Particular)")
    print("\t5.Delete Group")
    print("\t6.Exit")


@my_decorator
def manage_all_groups():
    while True:
        manage_all_group_menu()
        ch = int(input("\tEnter your choice "))
        if ch == 1:
            # Create group
            create_group()
        elif ch == 2:
            # display groups
            display_group()
        elif ch == 3:
            rename_group()
        elif ch == 4:
            # Manage group(Particular)
            manage_group()
        elif ch == 5:
            # Delete Group
            delete_group()
        elif ch == 6:
            # exit
            break
        else:
            print("\tInvalid choice")


@my_decorator
def create_group():
    group_name = input('\tEnter new group name : ')
    if group_name in group.keys():
        print('{group_name} group is already available on the system')
    else:
        group[group_name] = []
        print(f'{group_name} group created successfully ')


@my_decorator
def display_group():
    if len(group) == 0:
        print('There is no group available')
    else:
        for key, value in group.items():
            name_string = ""
            for i in value:
                name_string = name_string + "|" + emp[i]['name']
            # print('=' * 20)
            print(f'{key} -> {name_string}')
            print('=' * 10)


@my_decorator
def rename_group():
    group_name = input('\tEnter group name : ')
    if group_name not in group.keys():
        print(f'{group_name} group is not available on the system !')
    else:
        temp = group[group_name]
        n_grp_name = input('\tEnter new group name : ')
        del group[group_name]
        group[n_grp_name] = temp
        print(f'{n_grp_name} group name  updated successfully ')


@my_decorator
def delete_group():
    group_name = input('\tEnter group name : ')
    if group_name not in group.keys():
        print(f"{group_name} group not available on the system ! ")
    else:
        del group[group_name]
        print(f'{group_name} group deleted successfully')


@my_decorator
def manage_group_menu():
    print("\t\t1.Add Member")
    print("\t\t2.Delete Member")
    print("\t\t3.List Members")
    print('\t\t4.exit')


@my_decorator
def manage_group():
    group_name = input("\tEnter group name : ")
    if group_name not in group.keys():
        print(f'{group_name} group not on the syetem ! ')
    else:
        while True:
            manage_group_menu()
            ch = int(input('Enter your option: '))

            if ch == 1:
                add_member(group_name)
            elif ch == 2:
                delete_member(group_name)
            elif ch == 3:
                list_member(group_name)
            elif ch == 4:
                break
            else:
                print("Invalid option")


def add_member(group_name):
    display_data()
    serial_no = input('Enter serial number from above table : ')
    if serial_no not in emp.keys():
        print(f'\t{serial_no} serial number not available')
    else:
        group[group_name].append(serial_no)
    print(
        f'member added successfully on the {group_name}')


def list_member(group_name):
    if len(group[group_name]) == 0:
        print("no member found !")
    else:
        name_string = ""
        for i in group[group_name]:
            name_string = name_string + '|' + i + '.' + emp[i]['name']
        print(f'{name_string}')


def delete_member(group_name):
    list_member(group_name)
    serial_no = input('\tEnter serial number: ')
    if serial_no not in group[group_name]:
        print('\toops !!! wrong serial number ')
    else:
        group[group_name].remove(serial_no)
        print('employee removed from group')


while True:
    main_menu()
    ch = int(input('Enter choice : '))

    if ch == 1:
        # add employee data
        add_employee()

    elif ch == 2:
        # delete employee
        delete_employee()

    elif ch == 3:
        # search employee
        search_employee()

    elif ch == 4:
        # change employee data
        change_employee_data()
    elif ch == 5:
        # display data
        display_data()
    elif ch == 6:
        # manage all groups
        manage_all_groups()
    elif ch == 7:
        manage_org()
    elif ch == 8:
        break
    else:
        print('Invalid choice')
