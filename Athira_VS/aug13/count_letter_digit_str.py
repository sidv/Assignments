string = input("Enter a string with letters and digits: ")

a_count = 0
d_count = 0

for char in string:
	if char.isdigit():
		d_count += 1
	elif char.isalpha():
		a_count += 1
print(f"Total number of alphabets: {a_count}")
print(f"Total number of digits: {d_count}")