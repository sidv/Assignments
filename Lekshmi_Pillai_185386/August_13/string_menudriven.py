string = '''A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"
'''

def menu():
	print("1. Find the largest word")
	print("2. First Letter to upper and display it on terminal")
	print("3. Sorted by alphabetical order")
	print("4. Upper to Lower")
	print("5. Lower to Upper")
	print("6. Exit")
	
def largeword():
	strsplit = string.split(" ")
	length =0
	for i in range(0,len(strsplit)):
		if(strsplit[i]!=" " or strsplit[i]!='.'):
			if length < len(strsplit[i]):
				lengword = strsplit[i]
				length = len(strsplit[i])
	print (lengword)

def firstcaps():
	print(string.title())

def uppercase():
	print(string.upper())

def lowercase():
	print(string.lower())

def sorting():
	strsplit = string.split(" ")
	print(sorted(strsplit))
while True:
	menu()
	ch = int(input("Enter the choice"))
	if ch == 1:
		largeword()	
	elif ch == 2:
		firstcaps()
	elif ch ==3 :
		sorting()
	elif ch == 4:
		lowercase()
	elif ch == 5:
		uppercase()
	elif ch == 6:
		break
	else:
		print("Invalid Choice")
