while True:

	print("1.create file")
	print("2.write file")
	print("3.Delete file")
	print("4.Read file")
	print("5.Copy file")
	print("6.Find certain string inside a file")
	print("7.compare two file contents and print unique content of both file")
	print("8.Exit file")

	choice = int(input("Enter your choice : "))

	if choice == 1:
		file = input("enter filename")
		fd = open(file, "w")
		fd.close()

	if choice == 2:
		fname = input("Enter the file name to write content:")
		fd = open(fname, "w")
		data = input("Enter the content : ")
		fd.write(data)
		fd.close()

	if choice == 3:
		
		fname = input("enter the filename")
		fd = open(fname,"w")

		fd.close()

	if choice == 4:
				
		fname = input("Enter the file name and read the content")
		fd = open(fname,"r")
		data = input("Enter the content : ")
		fd.read()
		print(data)
		fd.close()
	if choice == 5:
		fname1 = input("Enter the first file name : ")
		fname2 = input("Enter the second file name : ")

		with open(fname1, "r") as fd1:
			with open(fname2, "w") as fd2:
				fd2.write(fd1.read())
		
	if choice == 6:
		fname1 = input("Enter the first file name : ")
		data = input("Enter the string for searching :")
		with open(fname1, "r") as fd:
			lines = fd.readlines()
			lst = lines[0].split("")
			for i in lst:
				if i == data:
					print(f"(data) found in file")
                   
                                
