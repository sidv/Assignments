frnds = ["Siddhant","Anubhav","Shweta","Rajat"]
nums=[10,20,30,40,50,60]

name = "Siddhant"

#for variable in range/object(Any iteratable data type)
#	statements
#	statements
#How to genrate range of numbers?
#range(start,end,step) 
#Start is included in range but end is excluded from range

for i in range(2,20,3):
	print(i)

for i in name: #Here iterating through each index of string
	print(i)

for name in frnds:
	print(name)

#Print even number from 10 to 50

for i in range(10,51):
	if i%2 == 0:
		print(i)
#Print summation of all numbers in list
sum=0
for i in nums:
	sum = sum + i
print(sum)

#Iterate through alternate letters of the string:
name = "Siddhant"
for i in name[::2]:
	print(i)

#Iterate through a part if list
for i in frnds[2:4]:
	print(i)
#Iterate through nested element
nested  = ["sid",[10,20],["Neha",30]]
for i in nested:
	for j in i :
		print(j)

















