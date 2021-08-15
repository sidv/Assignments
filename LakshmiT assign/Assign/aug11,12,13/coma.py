string = input("Enter the numbers with comma seperated")

num = string.split(",")
print(num)
sum = 0
for i in num:
	sum = sum + int(i)
print(sum)
