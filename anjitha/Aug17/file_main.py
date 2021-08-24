import file as f

while True:
	print("Enter 1 for create file")
	print("Enter 2 for write to file")
	print("Enter 3 for delete a file")
	print("Enter 4 for read a file")
	print("Enter 5 for copy a file")
	print("Enter 6 for comparison")
	print("Enter 7 for find")
	print("Enter 8 for Exit")
	
	ch = int(input("Enter choice"))
	if ch == 1:
		f.create_file()
	elif ch == 2:
		f.write_file()
	elif ch == 3:
		f.delete_file()
	elif ch == 4:
		f.read_file()
	elif ch == 5:
		f.copy_file()
	elif ch== 6:
		f.comp_file()
	elif ch== 7:
		f.find_file()
	elif ch == 8:
		break;
	else:
		print("Invalid Choice")
