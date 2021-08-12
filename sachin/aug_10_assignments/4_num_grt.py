num1=int(input("enter your first number :")) 
num2=int(input("enter your second number :")) 
num3=int(input("enter your third number :")) 
num4=int(input("enter your fourth number :")) 


if (num1 > num2) and (num1 > num3) and (num1 > num4):
    print("greatest num :",num1)
elif (num2 > num1) and (num2 > num3) and (num2 > num4):
    print("greatest num :",num2)
elif (num3 > num1) and (num3 > num2) and (num3 > num4):
    print("greatest num :",num3)
elif (num4 > num1) and (num4 > num2) and (num4 > num3):
    print("greatest num :",num4)    
else:
    print("invalid input")