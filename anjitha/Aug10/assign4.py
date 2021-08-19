
num=float(input("Enter the first num:"))
num1=float(input("Enter the second num:"))
operation=print("option 1 for addition")
operation=print("option 2 for multiplication") 
operation=print("option 3 for division") 
operation=print("option 4 for modulus") 
operation=print("option 5 for substraction") 
operation=print("option 6 for floor division") 
operation=input("Enter the operation:") 
if (int(operation) == 1):
	c=num+num1
	print(str(c))
elif (int(operation) == 2):
        c=num*num1
        print(str(c))
elif (int(operation) == 3):
        c=num/num1
        print(str(c))
elif (int(operation) == 4):
        c=num%num1
        print(str(c))
elif (int(operation) == 5):
        c=num-num1
        print(str(c))
elif (int(operation) == 6):
        c=num//num1
        print(str(c))



