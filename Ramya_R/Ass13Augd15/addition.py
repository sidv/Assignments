#2.Write a python code which accepts a sequence of comma seperated five numbers and find the addition of all of them

num=input("Enter seq of numbers: ") 
s=num.split(",")
print(s)

sum=0
for i in s:
	sum = sum+int(i)
print(sum)
