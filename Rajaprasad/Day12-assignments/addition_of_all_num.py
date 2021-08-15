num = "1,2,3,4,5,6,7,8,9"

print("______________Addition of all numbers __________________")

sum = 0
numbers = num[0::2]
print("numbers are " ,numbers)
for i in numbers:
	x = int(i)
	sum = sum+x

print("The sum is " ,sum)


print("_____________Addition of all even numbers______________")


even = num[2::4]
print("the even numbers are" , even)
sum = 0
for i in even:
	x = int(i)
	sum = sum+x

print("The even sum is " , sum)
