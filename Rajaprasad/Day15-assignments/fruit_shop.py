print('Fruit management system')

f = {}  # empty dictionary
cart = {}  # empty dictionary

# small decorator for displaying data


def my_decorator(func):

    def wrap_func():
        print('*'*30)
        func()
        print('*'*30)

    return wrap_func


@my_decorator
def main_menu():
    print("1.Add fruit ")
    print("2.Delete fruit by name")
    print("3.Search fruit by name and rate")
    print("4.change fruit name and rate")
    print("5.Display all fruit data")
    print("6.manage cart")
    print('7.exit')


@my_decorator
def add_fruit():
    s_no = int(input('Enter serial number : '))
    if s_no not in f.keys():
        f[s_no] = {
            'fruit_name': input("Enter fruit name : "),
            'Fruit_rate': int(input('Enter rate of fruit : ')),
            'imported_from': input('Enter import place of fruit : '),
            'imported_date': input('enter import date : '),
            'buy_price': float(input('enter buy price like xx.xx : '))
        }
        print('fruit added successfully')

    else:
        print('serial key already taken')


@my_decorator
def delete_fruit():
    s_no = int(input('enter serial number : '))
    if s_no not in f.keys():
        print('wrong serial number')
    else:
        del f[s_no]
        print("fruit deleted successfully")


@my_decorator
def search_fruit():
    print(' a,A => search by name \n b,B => search by rate')
    choice = input('enter choice: ')
    if choice == 'a' or choice == 'A':
        for i in f.values():
            name = input('Enter fruit name to search : ')
            if i['fruit_name'] == name:
                print(
                    f" {i['fruit_name']} |{i['Fruit_rate']} | {i['imported_from']} |{i['imported_date']} | {i['buy_price']}  ")
            else:
                print('wrong fruit name ')
    elif choice == 'b' or choice == 'B':
        for v in f.values():
            rate = float(input('provide rate for searching like xx.xx'))
            if v['fruit_rate'] == rate:
                print(
                    f"{v['fruit_name']} |{v['Fruit_rate']} | {v['imported_from']} |{v['imported_date']} | {v['buy_price']}  ")
            else:
                print('Not available with this price')


@my_decorator
def change_fruit():
    s_no = int(input('Enter serial number : '))
    if s_no not in f.keys():
        print('Please provide right serial number ')
    else:
        print('modify fruit data')
        f[s_no]['fruit_name'] = input('Enter new fruit name :')
        f[s_no]['fruit_rate'] = input('Enter new rate : ')
        print('fruit name modified successfully ')


@my_decorator
def display_fruit():
    if len(f) == 0:
        print('!' * 30)
        print('There is no fruit available')
    else:
        for i, j in f.items():
            print(
                f" {i} | {j['fruit_name']} |{j['Fruit_rate']} | {j['imported_from']} |{j['imported_date']} | {j['buy_price']}  ")


@my_decorator
def manage_cart_menu():
    print("\t1.Add item to cart")
    print("\t2.Delete item from cart")
    print("\t3.Display cart and bill")
    print("\t4.Exit")


@my_decorator
def add_to_cart():
    display_fruit()
    serial_no = int(input('Enter serial number: '))
    cart[serial_no] = f[serial_no]
    print(f'Fruit added in the cart successfully')


@my_decorator
def delete_from_cart():
    display_cart_and_bill()
    print('!'*30)
    s_no = int(input(('Enter fruit_id for delete fruit from cart : ')))
    del cart[s_no]
    print(f'fruit removed from cart !!!!')


@my_decorator
def display_cart_and_bill():
    if len(cart) == 0:
        print('!' * 30)
        print('There is no fruit available')
    else:
        sum = 0
        for i, j in cart.items():
            print(
                f" {i} | {j['fruit_name']} |{j['Fruit_rate']} | {j['imported_from']} |{j['imported_date']} | {j['buy_price']}  ")
            sum += j['buy_price']
        print('*'*20, f'price : {sum}', '*'*20)


@my_decorator
def manage_cart():
    while True:
        manage_cart_menu()
        ch = int(input("enter choice : "))
        if ch == 1:
            # add item to cart
            add_to_cart()

        elif ch == 2:
            # delete item from cart
            delete_from_cart()
        elif ch == 3:
            # display cart and bill
            display_cart_and_bill()

        elif ch == 4:
            # exit
            break


while True:
    main_menu()

    ch = int(input('Enter choice : '))

    if ch == 1:
        # add fruit
        add_fruit()

    elif ch == 2:
        # delete fruit name
        delete_fruit()
    elif ch == 3:
        # search fruit by name and rate
        search_fruit()

    elif ch == 4:
        # change fruit name and rate
        change_fruit()

    elif ch == 5:
        # display all fruits
        display_fruit()
    elif ch == 6:
        # manage cart
        manage_cart()

    elif ch == 7:
        break
    else:
        print('Invalid choice')
