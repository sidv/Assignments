import file

while True:
	print("press 1 for creating a file")
	print("press 2 for write data to file")
	print("press 3 for Delete data from file: ")
	print("press 4 for Read data from file: ")
	print("press 5 for copy content from one file to another ")
	print("press 6 for find string ")
	print("press 7 for comparison")
	print("press 8 for exit")
	choice = int(input("enter your choice"))
	
	if choice ==1:
		file.create_file()
	if choice ==2:
		file.write_file()
	if choice ==3:
                file.delete_content()
	if choice==4:
		file.read_file()
	if choice==5:
		file.copy_file()
	if choice==6:
		file.find_string()
	if choice==7:
		file.comp_file()
	if choice==8:
		break	
	else:
		print("INVALID")
	
