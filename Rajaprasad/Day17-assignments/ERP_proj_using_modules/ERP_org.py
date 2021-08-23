import ERP_org as org
org = {}  # empty dictionary


def my_decorator(func):

    def wrap_func():
        print('*'*30)
        func()
        print('*'*30)

    return wrap_func


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
