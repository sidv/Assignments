#Use Comprehensions or functions
string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"

def menu():
	print("1. Convert each alternate index word to upper case in above string")
	print("2. Remove alternate index word from above string")
	print("3. Find all the words from above string where first letter of word is 'c' and last letter is 'r'")
	print("4. Reverse all the words of above string")
	print("5. Find all the first letter of words from above string (No repetition of letters)")

def alter_index_upper():
	strsplit = string.split(" ")
	list1 = list(map(lambda x:x.upper(),strsplit[::2]))
	list2 = strsplit[1::2]
	index = 0
	for i in range(1,len(strsplit),2):
		list1.insert(i,list2[indx])	
		indx+=1
	print(" ".join(list1))
while True:
	menu()
	ch = int(input("Enter the choice"))
	if ch == 1:
		alter_index_upper()
	elif ch == 2:
		strsplit = string.split(" ")
		print(" ".join(strsplit[::2]))
	elif ch == 3:
		lst = string.split(" ")
		c_r_words = [i for i in lst if i[-1] == "r" and i[0] =="c"]
		print(c_r_words)
	elif ch == 4:
		lst = string.split(" ")
		reverse = [i[::-1] for i in lst]
		print(reverse)
	elif ch == 5:
		print({ i[0] for i  in string.split(" ")})
	elif ch == 6:
		print("Exit")
		break
	else:
		print("Invalid Choice")
		
