#Check number is between 10 to 20

num = int(input("Enter num"))

if num > 10 and num < 20: #If you want to execute your code only when both condition is true then use the "and" 
	print("Yes ! you number is correct")
else:
	print("Oops! Its worng")


if num == 10 or num == 15 or num == 17:
	print("Yes ! you guessed correct number")
else:
	print("Oops! Try next time")
