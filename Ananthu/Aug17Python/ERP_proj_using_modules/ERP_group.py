import ERP_member as m
import ERP_employee as em


group = {}  # empty dictionary


def my_decorator(func):

    def wrap_func():
        print('*'*30)
        func()
        print('*'*30)

    return wrap_func


group = {}  # empty dictionary


@my_decorator
def manage_all_group_menu():
    print("\t1.Create Group")
    print("\t2.Display Groups")
    print('\t3.rename group')
    print("\t4.Manage Group(Particular)")
    print("\t5.Delete Group")
    print("\t6.Exit")


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
                name_string = name_string + "|" + em.emp[i]['name']
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
def manage_group():
    group_name = input("\tEnter group name : ")
    if group_name not in group.keys():
        print(f'{group_name} group not on the syetem ! ')
    else:
        while True:
            m.manage_group_menu()
            ch = int(input('Enter your option: '))

            if ch == 1:
                m.add_member(group_name)
            elif ch == 2:
                m.delete_member(group_name)
            elif ch == 3:
                m.list_member(group_name)
            elif ch == 4:
                break
            else:
                print("Invalid option")
