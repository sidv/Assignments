print("ERP system")
emp = {}  # empty dictionary
group = {}  # empty dictionary


def main_menu():
    print("1.-Add Employee \n2.-Delete Employee \n3.-Search Employee by name \n4.-Change Employee Data \n5.Display \n6.manage all groups \n7.exit")


def add_employee():
    # add employee
    emp_id = 0
    serial_no = int(input('Enter serial no : '))
    emp_id += 1
    emp[serial_no] = {
        'emp_id': emp_id,
        'name': input("Enter employee name : "),
        'age': int(input('age : ')),
        'gender': input('gender : '),
        'salary': int(input('salary : ')),
        'previous_company': input('enter previous company name : '),
        'joining_date': input("Joining date : ")
    }
    print('Employee added successful')


def delete_employee():
    serial_no = int(input('Enter serial number: '))
    if serial_no not in emp.keys():
        print('please provide right serial number')
    else:
        del emp[serial_no]


def search_employee():
    name = input('Enter employee name for search : ')
    Flag = False
    for i in emp.values():
        if i['name'] == name:
            Flag = True
            print(f' { i["emp_id"] }| { i["name"]} | {i["age"]} | {i["gender"]} | {i["salary"]} | {i["previous_company"]}  | {i["joining_date"]} ')
    if Flag == False:
        print('employee not found')


def change_employee_data():
    serial_no = int(input('Enter serial number : '))
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


def display_data():
    print('Displaying all employees data')
    for i, v in emp.items():
        print('-'*10)
        print(
            f' { i }| { v["name"]} | {v["age"]} | {v["gender"]} | {v["salary"]} | {v["previous_company"]}  | {v["joining_date"]} ')
        print('-'*10)


def manage_all_group_menu():
    print("\t1.Create Group")
    print("\t2.Display Groups")
    print("\t3.Manage Group(Particular)")
    print("\t4.Delete Group")
    print("\t5.Exit")


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
            # Manage group(Particular)
            manage_group()
        elif ch == 4:
            # Delete Group
            delete_group()
        elif ch == 5:
            # exit
            break
        else:
            print("\tInvalid choice")


def create_group():
    group_name = input('\tEnter new group name : ')
    group[group_name] = []
    print(f'{group_name} group created successfully ')


def display_group():
    for key, value in group.items():
        name_string = ""
        for i in value:
            name_string = name_string + "|" + emp[i]['name']
        print('=' * 10)
        print(f'{key} -> {name_string}')
        print('=' * 10)


def delete_group():
    group_name = input('\tEnter group name : ')
    if group_name not in group.keys():
        print(f"{group_name} group not available ! ")
    else:
        del group[group_name]
        print(f'{group_name} group deleted successfully')


def manage_group_menu():
    print("\t\t1.Add Member")
    print('\t\t2.rename group')
    print("\t\t3.Delete Member")
    print("\t\t4.List Members")
    print('\t\t5.exit')


def manage_group():
    while True:
        group_name = input("\tEnter group name : ")
        manage_group_menu()
        ch = int(input('Enter your option: '))

        if ch == 1:
            add_member(group_name)
        elif ch == 2:
            rename_group(group_name)
        elif ch == 3:
            delete_member(group_name)
        elif ch == 4:
            list_member(group_name)
        elif ch == 5:
            break
        else:
            print("Invalid option")


def add_member(group_name):
    display_data()
    serial_no = int(input('Enter serial number from above table '))
    if serial_no not in emp.keys():
        print(f'\t\t{serial_no} serial number not available')
    else:
        group[group_name].append(serial_no)
        print(
            f'{group[group_name][serial_no]["name"]} added successfully on the {group_name}')


def rename_group(group_name):
    if group_name not in group.keys():
        print('this group is not available on the system')
    else:
        temp = group[group_name]
        n_grp_name = input('\t\tEnter new group name : ')
        del group[group_name]
        group[n_grp_name] = temp
        print(f'{n_grp_name} group name  updated successfully ')


def list_member(group_name):
    name_string = ""
    for i in group[group_name]:
        name_string = name_string + '|' + i + emp[i]['name']
    print(f'{name_string}')


def delete_member(group_name):
    list_member()
    serial_no = int(input('\t\tEnter serial number: '))
    if serial_no not in group[group_name]:
        print('\t\toops !!! wrong serial number ')
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
    elif ch == 6:
        break
    else:
        print('Invalid choice')
