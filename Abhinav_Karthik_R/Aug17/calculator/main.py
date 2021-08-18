import calc


def menu():
    Print("1.Addition \t 2.Subtraction")
    print("3.Multiplication \t 4.Division")
    print("5.Exit")

while True:
    menu()
    ch = int(input("Enter the choice"))
    a = int(input("Enter First number"))
    b = int(input("Enter Second number"))
    if(ch == 1):
        print(calc.add(a,b))
    elif(ch == 2):
        print(calc.sub(a,b))
    elif(ch == 3):
        print(calc.mul(a,b))
    elif(ch == 4):
        print(calc.div(a,b))
    elif(ch == 5):
        break
    else:
        print("Invalid input")
        