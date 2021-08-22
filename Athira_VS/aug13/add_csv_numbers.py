
num_list = input("Enter the comma separated numbers: ").strip().split(",")
#print(num_list)
sum = 0

for num in num_list:
	sum += int(num)
print(sum)