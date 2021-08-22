def create():
	filename = input("Enter the filename")
	fd = open(f"{filename}.txt","x")
	fd.close()
	
def writedata():
	filename = input("Enter the filename")
	file_content = input("Enter the Content")
	fd = open(f"{filename}.txt","w")
	fd.write(file_content)
	fd.close()

def deletedata():
	 filename = input("Enter the filename")
	 fd = open(f"{filename}.txt","w")
	 fd.close()
	 
def readdata():
	filename = input("Enter the filename")
	fd = open(f"{filename}.txt","r")
	filecontent = fd.read()
	print(filecontent)
	fd.close()

def copyfile():
	filename1 = input("Enter the filename")
	filename2 = input("Enter the filename")
	with open(f"{filename1}.txt","r") as f1:
		with open(filename2,"w") as f2:
			f2.write(f1.read())

def certain_string():
	filename1 = input("Enter the filename")
	string = input("Enter the string")
	with open(f"{filename1}.txt","r") as f1:
		content = (f1.read()).split(" ")
		lst = list(map(lambda a: "found" if a == string else "not found",content))
		print(lst)	

def compare_files():
	filename1 = input("Enter the filename")
	filename2 = input("Enter the filename")
	with open(f"{filename1}.txt","r") as f1:
		with open(f"{filename2}.txt","r") as f2:
			file1 = set((f1.read()).split(" "))
			file2 = set((f2.read()).split(" "))
			print(file1.symmetric_difference(file2))
			
			
		
		
		
		 
	
	
	
	
	
	
	
	
