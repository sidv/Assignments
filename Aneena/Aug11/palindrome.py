str = input("enter the text")
rev = str [::-1]
print("Text after reversing:" +rev)
if str == rev:
	print(str," is palindrome")
else:
	print(str,"is not a palindrome")
