# Program to print the fibanocci series for a given range given by user
limit = int(input("Enter the limit :"))
num1 = 0
num2 = 1
for x in range(limit):
	sum = num1 + num2
	num1 = num2
	num2 = sum
	print(num1)
