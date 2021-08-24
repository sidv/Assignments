print("___File handling___")

while True:
	print("1.create a file\n")
	print("2.write data to file\n")
	print("3.delete the file\n")
	print("4.read data from file\n")
	print("5.copy content to another file\n")
	print("6.search string from file\n")
	print("7.compare two files content print unique content of both file\n")
	print("8.exit")
	

	choice=int(input("Enter choice\n"))
	if choice == 1:
		file=input("file name")
		fd=open(f"{file}.txt","x")
		fd.close()

	elif choice == 2:
		wfile=input("file name")
		fd=open(f"{wfile}.txt","w")
		data=input("Enter the data\n")
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
		file1=input("Enter file name of data")
		file2=input("Enter destination file")
		with open(f"{file1}.txt","r") as f1:
			with open(f"{file2}.txt","w") as f2:
				f2.write(f1.read())


	elif choice ==6:
		sfile=input("Enter file to be search")
		sdata=input("Enter string to search")
		with open(f"{sfile}.txt","r") as f1:
			for i in f1.read().split(" "):
				if i == sdata:
					print("Found!")
				else:
					print("Not found!")

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
