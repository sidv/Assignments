string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"

def menu():
	print("1. Write the above string into file data1.txt")
	print("2. Write the above string alternate index words into the file data2.txt")
	print("3. Write the code to find all the words in data1.txt but not in data2.txt")
	print("4. Write the above string into 10 files data3.txt,data4.txt and so on.. ")
	print("5. Exit")
	
def write_string():
	with open("data1.txt","w") as fd:
		fd.write(string)

def alternative_index():
	lst = []
	strsplit = string.split(" ")
	with open("data2.txt","w") as fd:
		strsplit = string.split(" ")
		lst = list(filter(lambda x:strsplit.index(x)%2==0,strsplit))
		new_str = " ".join(lst)
		fd.write(new_str)
def file_difference():
	with open("data1.txt","r") as fd1:
		with open("data2.txt","r") as fd2:
			file1 = set(fd1.read().split(" "))
			file2 = set(fd2.read().split(" "))
			print(file1.difference(file2))

def copy_file():
	for i in range(3,13):
		fd1 = open(f"data{i}.txt","w")
		fd1.write(string)
		fd1.close()
while True:
	menu()
	ch = int(input("Enter the choice"))
	if ch == 1:
		write_string()
	elif ch == 2:
		alternative_index()
	elif ch == 3:
		file_difference()
	elif ch == 4:
		copy_file()
	elif ch == 5:
		break
	else:
		"Invalid choice"
	
