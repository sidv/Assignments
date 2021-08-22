while True:
    print("\n\n__________MENU__________\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. EXIT")
    op = int(input())
    if op == 7:
        break
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    if op == 1:
        print(num1, "+", num2, "=", num1+num2)
    elif op == 2:
        print(num1, "-", num2, "=", num1-num2)
    elif op == 3:
        print(num1, "*", num2, "=", num1*num2)
    elif op == 4:
        print(num1, "/", num2, "=", num1/num2)
    elif op == 5:
        print(num1, "//", num2, "=", num1//num2)
    elif op == 6:
        print(num1, "%", num2, "=", num1%num2)
    else:
        print("Invalid choice")
