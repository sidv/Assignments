num1=int(input("Enter frist num:"))
num2=int(input("Enter second num:"))
num3=int(input("Emter third num:"))
num4=int(input("Enter fourth num:"))

if (num1 > num2 and num1 > num3 and num1 > num4):
	print(str(num1)+"is greater")
elif (num2 > num1 and num2 > num3 and num2 > num4):
	print(str(num2) +"is greater")
elif (num3 > num1 and num3 > num4 and num3 > num2):  
	print(str(num3) +"is greater")
else:
	 print(str(num4) +"is greater") 
 
