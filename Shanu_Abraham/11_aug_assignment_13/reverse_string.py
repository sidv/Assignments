#Prgram to find the given string is palindrom or not
str = input("Enter the string")
rev_str=str[::-1]
if (str==rev_str):
	print("The given string is reversed")
else:
	print("It is not reversed")
