print("file handling")

while True:
	print("1 for create a file")
	print("2 for write data to file")
	print("3 for delete the file")
	print("4 for read data from file")
	print("5 for copy content to another file")
	print("6 for find certain string from file")
	print("7 for compare two files content print unique content of both file")
	print("8 for exit")
	

	choice=int(input("enter choice"))
	if choice == 1:
		file=input("file name")
		fd=open(f"{file}.txt","x")
		fd.close()

	elif choice == 2:
		wfile=input("file name")
		fd=open(f"{wfile}.txt","w")
		data=input("enter data")
		fd.write(data)
		fd.close()
	elif choice == 3:
		dfile=input("File name to delete")
		fd=open(f"{dfile}.txt","w")
		fd.close()
	elif choice ==4:
		rfile=input("File name to read")
		fd=open(f"{rfile}.txt","r")
		data=fd.read()
		print(data)
	elif choice ==5:
		file1=input("enter file name of data")
		file2=input("enter destination file")
		with open(f"{file1}.txt","r") as f1:
			with open(f"{file2}.txt","w") as f2:
				f2.write(f1.read())


	elif choice ==6:
		sfile=input("Enter file to be search")
		sdata=input("enter string to search")
		with open(f"{sfile}.txt","r") as f1:
			for i in f1.read().split(" "):
				if i == sdata:
					print("found")
				else:
					print("not found")

	elif choice ==7:
		cfile1=input("Enter file name")
		cfile2=input("Enter 2nd file name")
		with open(f"{cfile1}.txt","r") as f1:
			with open(f"{cfile2}.txt","r") as f2:
				file1=set(f1.read().split(" "))
				file2=set(f1.read().split(" "))
				print(file1.symmetric_difference(file2))

	elif choice ==8:
		break;
