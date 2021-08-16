#3.Write a python code to print comma seperated fibinacci numbers(1,1,2,3,5,8,11)(Take limit from user)

rangenum = int(input("Enter the number"))

num1 = 0
num2 = 1
count = 0
lst = []
if rangenum <= 0:
	print ("Enter valid range")
	
elif rangenum == 1:
	print (num1)

else:
	print("Fibonacci Series")
	while(count<rangenum):
		lst.append(str(num1))
		num3 = num1+num2
		num1 = num2 
		num2 = num3
		count+=1
	print(",".join(lst))
