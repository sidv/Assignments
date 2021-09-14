
def files_menu():
	print("Enter your choice")
	print("1.Create file")
	print("2.Write data into file")
	print("3.Delete data from file")
	print("4.Read data from file")
	print("5.Copy content of string")
	print("6.Search string")
	print("7.Exit")
def create_file():
	name = input("Enter the name of the file to be created")
	fd = open(name,"x")
	fd.close()
	print(f"File with name {name} created!")
def write_file():
	name = input("Enter the file name")
	data = input("Enter the data to be added")
	fd = open(name,"w")
	fd.write(data)
	fd.close()
	print("Data written succesfully!!")
def delete_data():
	name = input("Enter the file to delete data from")
	fd=open(name,"w")
	fd.write(" ")
	fd.close()
def read_data():
	name=input("Enter the file to read")
	fd = open(name,"r")
	print(fd.read())
	fd.close()
def copy_content():
	name1 = input("Enter the name of the new file")
	name2 = input("Enter the file to copy from")
	ld = open(name,"x")
	ld.close()
	with open(name2,"r") as fd_1:
		with open(name1,"w") as fd_2:
			fd_2.write(fd1.read())
def find_string():
	pass
	
def compare_files():
	pass
	

	
