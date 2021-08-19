#3.Write a python code to print comma seperated fibinacci numbers(1,1,2,3,5,8,11)(Take limit from user)
n = int(input("Enter range upto which number u want: "))
a = 0
b = 1
f = 1
out = []
count = 0
#print("series")
while b <= n:
	#out.append(str(a))
	f=a+b
	a=b
	b=f
	out.append(str(a))
	#count+=1
print(",".join(out))



