import file
while True:
	print("Enter 1 for create file")
	print("Enter 2 for write data to file")
	print("Enter 3 for delete data from file")
	print("Enter 4 for read data from file")
	print("Enter 5 for copy content of file to another file")
	print("Enter 6 for find string inside a file")
	print("Enter 7 for compare 2 files")
	print("Enter 8 to exit")
	
	ch = int(input("Enter the choice : "))
	
	if ch ==1:
		name = input("Enter the name of file : ")
		file.create(name)
	elif ch==2:
		name = input("Enter the name of the file : ")
		data = input("Enter the data to write : ")
		file.write_data(data,name)
	elif ch==3:
		name = input("Enter the name of the file : ")
		file.delete_data(name)
	elif ch==4:
		name = input("Enter the name of the file : ")
		file.read_data(name)
	elif ch==5:
		n1 = input("Enter the name of the 1st file : ")
		n2 = input("Enter the name of the 2nd file : ")
		file.copy(n1,n2)	 
	elif ch==6:
		n = input("Enter the name of the file : ")
		s = input("Enter the string : ")
		file.find(n,s)
	elif ch==7:
		n1 = input("Enter the name of the 1st file : ")
		n2 = input("Enter the name of the 2nd file : ")
		file.compare(n1,n2)
	elif ch==8:
		break
	else:
		print("invalid choice")
