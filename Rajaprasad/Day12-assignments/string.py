print("3.Write a program to check given string ends with 't' or not ")

str1 = input("Enter a string")

if str1:
	if str1[-1] == 't' :
		print("string last letter is t")
	else:
		print("provide another string which last letter has t")
else:
	print("Enetr a string once more")
str2 = input("Enter a string : " )

if str2 :
	if str2[-3:] == 'lis':
		print("string last 3 letter is lis")
	else:
		print(" string last 3 letter is not lis")
else:
	print("enter another string") 

