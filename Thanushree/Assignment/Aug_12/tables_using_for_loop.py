num = int(input("Enter the num "))
print("The multiplication table of:",num)
for count in range(1,11):
	product=count*num
	print(f"{num} * {count} = {product}")
