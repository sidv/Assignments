def create_file():
	file=input("Enter file name : ")
	fd=open(file,"w")
	fd.close()
def write_file():
	f_name=input("Enter the  file name to write the content : ")
	fd=open(f_name,"w")
	data=input("Enter the content: ")
	fd.write(data)
	fd.close()
def delete_content():
	f_name=input("Enter the  file name to delete the content : ")
	fd=open(f_name,"w")
	fd.truncate()
def read_file():
	f_name=input("Enter the  file name to you want to read : ")
	fd=open(f_name,"r")
	print(fd.read())
	fd.close()
def copy_file():
	f_name=input("Enter the file name you want to copy : ")
	new_f_name=input("Enter the other file name : ")
	with open("f_name","r")as f:
		with open("new_f_name","a")as fa:
			for i in f:
				fa.write(i)
		fa.close()
		f.close()
def find_string():
	with open(file, 'r') as f:
		x = input("Enter string to find")
	for i in f.read().split(" "):
		if i == x:
			new_file = input("Enter new file name to copy content : ")
		with open(new_file, 'w') as f2:
			f2.write(i)

def comp_file():
	with open(file, 'r') as f:
		f_name = input("enter another filename to find unique element : ")
	with open(f_name, 'r') as f_name:
		print(set(f.read()).symmetric_difference(set(f_name.read())))
