def create():
	filename = input("Enter the filename: ")
	fd = open(f"{filename}.txt","x")
	fd.close()

def write():
	filename = input("Enter the filename: ")
	content = input("Enter the Contentu want to write: ")
	fd = open(f"{filename}.txt","w")
	fd.write(content)
	fd.close()

def delete():
	 filename = input("Enter the filename: ")
	 fd = open(f"{filename}.txt","w")
	 fd.close()

def read():
	filename = input("Enter the filename: ")
	fd = open(f"{filename}.txt","r")
	content = fd.read()
	print(content)
	fd.close()

def copy():
	filename1 = input("Enter the filename1: ")
	filename2 = input("Enter the filename2: ")
	with open(f"{filename1}.txt","r") as f1:
		with open(filename2,"w") as f2:
			f2.write(f1.read())

def certain_string():
	filename1 = input("Enter the filename1: ")
	string = input("Enter the string: ")
	with open(f"{filename1}.txt","r") as f1:
		content = (f1.read()).split(" ")
		lst = list(map(lambda a: "found" if a == string else "not found",content))
		#lst = list(filter(lambda a: "found" if a == string else "not found",content))
		print(lst)	

def compare_files():
	filename1 = input("Enter the filename1: ")
	filename2 = input("Enter the filename: ")
	with open(f"{filename1}.txt","r") as f1:
		with open(f"{filename2}.txt","r") as f2:
			file1 = set((f1.read()).split(" "))
			file2 = set((f2.read()).split(" "))
			print(file1.symmetric_difference(file2))









