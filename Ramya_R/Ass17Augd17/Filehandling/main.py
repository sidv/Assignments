import file as f


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
		f.create()
	elif ch == 2:
		f.write()
	elif ch == 3:
		f.delete()
	elif ch == 4:
		f.read()
	elif ch == 5:
		f.copy()
	elif ch == 6:
		f.certain_string()
	elif ch == 7:
		f.compare_files()
	elif ch == 8:
		break
	else:
		print("Invalid choice")
