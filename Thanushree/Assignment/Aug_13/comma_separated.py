str = str(input("Enter the five numbers"))
numbers = str.split(",")
print(numbers)
sum = 0
for i in numbers:
	sum = sum + int(i)
print(sum)
