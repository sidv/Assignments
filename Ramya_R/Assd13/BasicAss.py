
i = int(input("Enter which table u want: "))
for n in range(1,11):
	print(i,"*",n,"=",n*i)
print("-------------even no--------------")

sr=int(input("enter your Start range: "))
er=int(input("enter your end range: "))
for x in range(sr,er):
	if x%2 == 0:
		print(x)
print("------------odd no----------")

for y in range(sr,er):
	if y%2 != 0:
		print(y)
print("--------fibonnaci series----")

a=0
b=1
f=1
n=100
while b <= n:
	f=a+b
	a=b
	b=f
	print(a)


