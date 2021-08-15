#print table if num given by user
num = int(input("Enter the num"))

#Print table from 1 to 10

count = 1
while count < 11: #Here expression must be evaluated to true or false
	res = count * num
	print(res)
	count = count+1 #count+=1
#Infinite while loop:
#while True : #Here this while loop will iterate for infinite times because condition is always true
#	count=count+1
#	print(count)
