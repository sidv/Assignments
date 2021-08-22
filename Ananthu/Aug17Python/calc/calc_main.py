from typing import SupportsBytes
import menu as m
import calc_opr as c
print(
    "4.Write a menu driven calculator, Addition,Substraction,Muliplication,Divison,Floor divison,Modulas(Try float values for all operation)")

while True:
    m.menu()
    choice = int(input("Enter a choice from 1 to 6 : "))
    num1 = float(input("Enter 1st number : "))
    num2 = float(input("Enter 2nd number : "))
    if choice == 1:
        c.add(num1, num2)
    elif choice == 2:
        c.sub(num1, num2)
    elif choice == 3:
        c.mul(num1, num2)
    elif choice == 4:
        c.div(num1, num2)
    elif choice == 5:
        c.modulus(num1, num2)
    elif choice == 6:
        c.floor(num1, num2)

    else:
        print("Invalid option")
