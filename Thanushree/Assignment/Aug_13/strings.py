string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"
def main_menu():
	print("1. To find the largest word in the above string")
	print("2. To convert first letter of each word to upper case and display it on terminal")
	print("3. To print string on terminal in sorted alphabetical order")
	print("4. Uppercase to Lowercase")
	print("5. Lowercase to Uppercase")
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
