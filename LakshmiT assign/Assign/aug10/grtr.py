num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
num4 = int(input("Enter 4th number: "))

if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print(str(num1) + " is the largest")
        else:
            print(str(num4) + " is the largest")
    else:
        if num3 > num4:
            print(str(num3) + " is the largest")
        else:
            print(str(num4) + " is the largest")
else:
    if num2 > num3:
        if num2 > num4:
            print(str(num2) + " is the largest")
        else:
            print(str(num4) + " is the largest")
    else:
        if num3 > num4:
            print(str(num3) + " is the largest")
        else:
            print(str(num4) + " is the largest")
