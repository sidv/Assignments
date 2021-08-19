
def create_file():
	name=input("Enter the file name you want to create:")
	f=open(name,"x")
	f.close()
	print("file created successfully")
	
def write_file():
	nam=input("Enter the file name you want to write:")
	fdr =open("nam","w")
	para=input("Enter the content you want write:")
	fdr.write(para)
	fdr.close()
	print("file modified successfully")
	
def delete_file():
	nam=input("Enter the file name you want to delete:")
	f =open("nam","w")
	f.truncate()
	print("file deleted successfully")
def read_file():
	nam=input("Enter the file name you want to read:")
	fdr =open("nam","r")
	print(fdr.read())
	fdr.close()
def copy_file():
	nam=input("Enter the file name you want to copy:")
	name=input("Enter the file new name:")
	with open("nam","r") as f:
		with open("name","a") as fa:
			for i in f:
				fa.write(i)
				print("file copied successfully")
		
	
def comp_file():
	nam=input("Enter the first file name")
	name=input("Enter the second file name")
	with open("nam","r") as f:
		with open("name","r") as fi:
			for i in f:
				for j in fi:
					if i==j:
						print(i)
					else:
 						print("Not found!!")
	
def find_file():
	nam=input("Enter the file name you want to check:")
	para=input("Enter the dtring you want to find!!!:")
	with open("nam","r") as f:
		if para in f.read():
			print(f"{para} is found the file!!")
	
		else:
			print(f"{para} is not found in the file!!")
	






