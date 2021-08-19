string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"

def menu():
	print("1. Convert each alternate index word to upper case")
	print("2. Remove alternate index word from above string")
	print("3. Find all the words from above string where first letter of word is 'c' and last letter is 'r'")
	print("4. Reverse all the words of above string")
	print("5. Find all the first letter of words from above string (No repetition of letters)")
	print("6. Exit")
	
while True:
	menu()
	ch = int(input("Enter the choice"))
	if ch == 1:
		strsplit = string.split(" ")
		lst = strsplit[::2]
		list1 = list(map(lambda x:x.upper(),lst))
		print(" ".join(list1))
	elif ch == 2:
		strsplit = string.split(" ")
		lst = strsplit[::2]
		print(" ".join(lst))
	elif ch == 3:
		lst = string.split(" ")
		print(list(filter(lambda a: a[-1] == "r" and a[0] == "c",lst)))
	elif ch == 4:
		print(list(map(lambda a: a[::-1],string.split(" "))))
	elif ch == 5:
		print(set(map(lambda a: a[0],string.split(" "))))
	elif ch == 6:
		break
	else:
		"Invalid choice"
