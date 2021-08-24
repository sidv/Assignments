#4.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are #divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

binary = [1000,1111,1101,1010]
lst= []
for i in binary:
	a = int(str(i),2)
	if a % 5 ==0:
		lst.append(i)
print(lst)
