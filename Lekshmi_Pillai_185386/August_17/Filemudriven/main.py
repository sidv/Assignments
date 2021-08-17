import fileopn

def menu():
	print("1. Create file")
	print("2. Write data to file")
	print("3. Delete data from file")
	print("4. Read data from file")
	print("5. Copy content of one file to another")
	print("6. Find certain string inside a file")
	print("7. Compare two files and print unique content ")
	print("8. Exit")
	
while True:
	menu()
	ch =  int(input("Enter the choice"))
	if ch == 1:
		fileopn.create()
	elif ch == 2:
		fileopn.writedata()
	elif ch == 3:
		fileopn.deletedata()
	elif ch == 4:
		fileopn.readdata()
	elif ch == 5:
		fileopn.copyfile()
	elif ch == 6:
		fileopn.certain_string()
	elif ch == 7:
		fileopn.compare_files()
	elif ch == 8:
		break
	else:
		print("Invalid choice")
