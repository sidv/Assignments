import ERP_employee as em
import ERP_group as eg


def my_decorator(func):

    def wrap_func():
        print('*'*30)
        func()
        print('*'*30)

    return wrap_func


@my_decorator
def manage_group_menu():
    print("\t\t1.Add Member")
    print("\t\t2.Delete Member")
    print("\t\t3.List Members")
    print('\t\t4.exit')


def add_member(group_name):
    em.display_data()
    serial_no = input('Enter serial number from above table : ')
    if serial_no not in em.emp.keys():
        print(f'\t{serial_no} serial number not available')
    else:
        eg.group[group_name].append(serial_no)
    print(
        f'member added successfully on the {group_name}')


def list_member(group_name):
    if len(eg.group[group_name]) == 0:
        print("no member found !")
    else:
        name_string = ""
        for i in eg.group[group_name]:
            name_string = name_string + '|' + i + '.' + em.emp[i]['name']
        print(f'{name_string}')


def delete_member(group_name):
    list_member(group_name)
    serial_no = input('\tEnter serial number: ')
    if serial_no not in eg.group[group_name]:
        print('\toops !!! wrong serial number ')
    else:
        eg.group[group_name].remove(serial_no)
        print('employee removed from group')
