while True:
	print("1.create file")
	print("2.write file")
	print("3.delete file")
	print("4.read file")
	print("5.copy file")
	print("6.exit")
	choice = int(input("enter your choice"))
	if choice == 1:
		file=input("enter file name")
		f=open(file,"w")
		f.close()
	if choice == 2:
		fname=input("enter your file name to write")
		f=open(fname,"w")
		data= input("enter the content:")
		f.write(data)
		f.close()
	if choice == 3:
		fname=input("enter your file name to write")
		f=open(fname,"w")
		f.close()
	if choice == 4:
		fname=input("enter your file to read")
		f=open(fname,"r")
		data=f.read()
		print(data)
		f.close()
	if choice == 5:
		fname1 = input("enter the first file name")
		fname2 = input("enter the second file name")
		with open(fname1, "r") as fd1:
			with open(fname2, "w") as fd2:
				fd2.write(fd1.read())
	if choice == 6:
		fname1 = input("enter the file name")
		data = input("enter the string for searching")
		with open(fname1, "r") as fd:
		lines = fd.readlines()
		lst = lines[0].split(" ")
		for i in lst:
			if i == data:
				print(f"{data} found in file")

