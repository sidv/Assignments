from calc import *

while True:
    print("______MENU______")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulo Division")
    print("7. Exit")

    ch = input("Enter your choice: ")

    if ch and ch != '7':
        a = int(input("Enter num1: "))
        b = int(input("Enter num2: "))

    if ch == '1':
        print(add(a, b))
    elif ch == '2':
        print(subtract(a, b))
    elif ch == '3':
        print(multiply(a, b))
    elif ch == '4':
        print(divide(a, b))
    elif ch == '5':
        print(floor_divide(a, b))
    elif ch == '6':
        print(modulo_divide(a, b))
    elif ch == '7':
        break
    else:
        print("Invalid Entry!!!")
