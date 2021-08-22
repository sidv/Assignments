print("STRING PALINDROME")

a = input("Enter a string  : ")

rev = a[::-1]
if a == rev:
	print("String reverse is : ",rev)
	print(a,"is PALINDROME")
