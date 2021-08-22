#2.Write a python code which accepts a sequence of comma seperated five numbers and find the addition of all of them
string = input("Enter the numbers with comma seperated")

num = string.split(",")
print(num)
sum = 0
for i in num:
	sum = sum + int(i)
print(sum)
