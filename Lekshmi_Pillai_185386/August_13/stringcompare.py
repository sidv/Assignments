string1 = '''A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"
'''
string2 = '''A broad range of industrial and consumer products use computers as control systems. Simple special-purpose devices like microwave ovens and remote controls are included, as are factory devices like industrial robots and computer-aided design, as well as general-purpose devices like personal computers and mobile devices like smartphones. Computers power the Internet, which links hundreds of millions of other computers and users. '''

def menu():
	print("1. Find all the common words in above string1 and string2")
	print("2. Find all the words available in string1 but not available in string2")
	print("3. Find all the unique words in above string1 and string2")
	print("4. Append all words from above string2 to string1 if they are not in string1")
	print("5. Exit")
	
def commonword(strsplit1,strsplit2):
	print(strsplit1.intersection(strsplit2))

def differenceset(strsplit1,strsplit2):
	print(strsplit1.difference(strsplit2))
	
def uniquewords(strsplit1,strsplit2):
	print((strsplit1.union(strsplit2)).difference(strsplit1.intersection(strsplit2)))
	print(strsplit1.symmetric_difference(strsplit2))
	
def appendstring(strsplit1,strsplit2):
	print(strsplit1.union(strsplit2.difference(strsplit1)))
	
while True:
	menu()
	strsplit1 = set(string1.split(" "))
	strsplit2 = set(string2.split(" "))
	ch = int(input("Enter the choice"))
	if ch == 1:
		commonword(strsplit1,strsplit2)
	elif ch == 2:
		differenceset(strsplit1,strsplit2)
	elif ch ==3 :
		uniquewords(strsplit1,strsplit2)
	elif ch == 4:
		appendstring(strsplit1,strsplit2)
	elif ch == 5:
		break
	else:
		print("Invalid Choice")
