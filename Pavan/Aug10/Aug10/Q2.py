num="1,2,3,4,5,6,7,8,9"

numlist=num.split(',')

print(numlist)

print(numlist[1::2])


for i in numlist:
	print(i,end=" ")
print(" ")

for i in numlist[1::2]:
	print(i,end=" ")
print("\n")
add_res=int(numlist[0])+int(numlist[4])
mul_res=int(numlist[1])*int(numlist[7])

print(add_res)
print(mul_res)
