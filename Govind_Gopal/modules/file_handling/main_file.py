import files as f

while True:
	f.files_menu()
	ch = input("Enter your choice")
	
	if ch == "1":
		f.create_file()
	elif ch == "2":
		f.write_file()
	elif ch == "3":
		f.delete_data()
	elif ch == "4":
		f.read_data()	
	elif ch == "5":
		f.copt_content()
	elif ch == "6":
		pass
	elif ch == "7":
		break
	else:
		print("Invalid input")
		
