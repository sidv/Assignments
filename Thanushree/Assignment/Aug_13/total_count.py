str = input("Enter the string")
d_count=0
l_count=0
for i in str:
	if i.isdigit():
		d_countt +=1
	elif (i == " " or  i == "."):
		pass
	else:
		l_count+=1
print(f"Total digits in the string => {d_count}")
print(f"Total letters in the string => {l_count}")
