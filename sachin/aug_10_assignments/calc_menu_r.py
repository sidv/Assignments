while True:

    print("Press 1 for add")
    print("Press 2 for substract")
    print("press 3 for multiplication")
    print("press4 for division")
    print("press5 for Floor divison")
    print("press6 for Modulas")


    choice = int(input("Enter choice : "))
    if choice != 7: # != means not equal to
        num1 = float(input("Enter number 1 :"))
        num2 = float(input("Enter number 2 :"))


    if choice == 1: #Its equal to
        res = num1 + num2
        print(res)
        
    if choice == 2: 
        res = num1 - num2
        print(res)  
    if choice == 3: 
        res = num1 * num2
        print(res)
    if choice == 4: 
        res = num1 / num2
        print(res)                      
    if choice == 5: 
        res = num1 // num2
        print(res)
    if choice == 6: 
        res = num1 % num2
        print(res)
    elif choice == 7:
        break
    else:
	    print("-----------")