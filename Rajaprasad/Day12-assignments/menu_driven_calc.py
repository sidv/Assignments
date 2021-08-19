print("4.Write a menu driven calculator, Addition,Substraction,Muliplication,Divison,Floor divison,Modulas(Try float values for all operation)")

while True:

        print("1.addition 2.substraction 3.multiplicatio 4.division 5.modulus 6.floor division")
        choice=int(input("Enter a choice from 1 to 6 : "))
        num1=int(input("Enter 1st number"))
        num2=int(input("Enter 2nd number"))

        if choice == 1:
                print(f'{num1} + {num2} ={num1+num2}')


        elif choice == 2:
                print(f'{num1} - {num2} ={num1-num2}')

        elif choice == 3:
                print(f'{num1} * {num2} = {num1*num2}')

        elif choice == 4:
                print(f'{num1} / {num2} = {num1/num2}')

        elif choice == 5:
                print(f'{num1} % {num2} = {num1%num2}')
        elif choice == 6:
                print(f'{num1} // {num2} = {num1 // num2}')

        else:
                print("Invalid option")




