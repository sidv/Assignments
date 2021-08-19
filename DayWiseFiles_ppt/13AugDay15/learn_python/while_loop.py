#print table if num given by user
num = int(input("Enter the num"))

#Print table from 1 to 10

count = 1
#while count < 11: #Here expression must be evaluated to true or false
#	res = count * num
#	print(res)
#	count = count+1 #count+=1
#Infinite while loop:
#while True : #Here this while loop will iterate for infinite times because condition is always true
#	count=count+1
#	print(count)


#while True:
#	count = count+1
#	print(count)
#	if count == 100:
#		break
count=0
while  count < 11:
	if count >= 4 and count <=8:
		count += 1
		continue
	print(count * num)
	count +=1

while count < 11:
	count+=1
	pass

#for i in lst:
#	pass

def manage_data():
	pass

num = int(input("Enter number"))

#if num > 10:
#	print("num is greater than 10")
#else:
#	print("num is less than 10")

while num > 10:
	num-=1
	print(num)
else:
	print("Num is less 10 please enter greater value")



