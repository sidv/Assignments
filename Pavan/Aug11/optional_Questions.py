print("\n____________Question 1_______________\n")

num=int(input("Enter the desired number\n"))
limit=int(input("Enter the limit\n"))
for i in range(limit+1):
	print(str(i)+"x"+str(num)+"="+str(num*i))

print("\n____________Question 2_______________\n")

num=int(input("Enter required range.\n"))
for i in range(num+1):
	if i%2 ==0:
		print(i)

print("\n____________Question 3_______________\n")

num=int(input("Enter required range.\n"))
for i in range(num+1):
        if i%2 !=0:
                print(i)

print("\n____________Question 4_______________\n")

num=int(input("Enter required range.\n"))
i=0
j=1
f=0
print(i)
while f<num:
	print(i)
	g=i+j
	i=j
	j=g
	f=f+1

print("\n____________Question 5_______________\n")

s=list(input("Enter required string.\n"))
print(s)
x=s.copy()
print(x)
s.reverse()
if x==s:
        print("It is a Palindrome.\n")
else:
        print("No, its not.\n")


print("\n____________Question 6_______________\n")

num1=int(input("Enter the divident.\n"))
num2=int(input("Enter the divisor.\n"))

if num1%num2==0:
	print("Divisible\n")
else:
	print("Not Divisible\n")
