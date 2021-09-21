import ERP_employee as em
import ERP_org as org
import ERP_group as eg
import ERP_member as m


print(" " * 10, "ERP system")

# small decorator for displaying data


def my_decorator(func):

    def wrap_func():
        print('*'*30)
        func()
        print('*'*30)

    return wrap_func


def manage_org():

    while True:
        org.manage_org_menu()
        ch = int(input("Enter choice : "))
        if ch == 1:
            # create organisation
            org.create_org()
        elif ch == 2:
            # modify organisation
            org.modify_org_name()
        elif ch == 3:
            # show organisation
            org.show_org()
        elif ch == 4:
            break
        else:
            print("Invalid option")


@my_decorator
def manage_all_groups():
    while True:
        eg.manage_all_group_menu()
        ch = int(input("\tEnter your choice "))
        if ch == 1:
            # Create group
            eg.create_group()
        elif ch == 2:
            # display groups
            eg.display_group()
        elif ch == 3:
            eg.rename_group()
        elif ch == 4:
            # Manage group(Particular)
            eg.manage_group()
        elif ch == 5:
            # Delete Group
            eg.delete_group()
        elif ch == 6:
            # exit
            break
        else:
            print("\tInvalid choice")


while True:
    em.main_menu()
    ch = int(input('Enter choice : '))

    if ch == 1:
        # add employee data
        em.add_employee()

    elif ch == 2:
        # delete employee
        em.delete_employee()

    elif ch == 3:
        # search employee
        em.search_employee()

    elif ch == 4:
        # change employee data
        em.change_employee_data()
    elif ch == 5:
        # display data
        em.display_data()
    elif ch == 6:
        # manage all groups
        manage_all_groups()
    elif ch == 7:
        manage_org()
    elif ch == 8:
        break
    else:
        print('Invalid choice')
