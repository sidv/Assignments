print("Q1&2 Optional questions\n")

num=int(input("Enter input num to whether find if its odd or not.\n"))

if(num%2==0):
	print(str(num)+" is even.")
else:
	print(str(num)+" is odd.")

print("\n\n___________3.) Optional Question____________\n")

var=input("Enter required string\n")

if(var[-1]=="t"):
	print("Yes "+ var + " does ends with t.")
else:
	print("No")

print("\n\n___________4.) Optional Question____________\n")

var2=input("Enter required string\n")
if(var2[-3:]=="iis"):
	print("Yes "+ var + " does ends with iis.")
else:
	print("No")

print("\n\n___________Q5&6.) Optional Questions____________\n")

sum_even=0
sum_odd=0
i=0

while i<21:
	if(i%2==0):
		sum_even+=i
	else:
		sum_odd+=i
	i+=1
print(sum_even,sum_odd)
