with open("mybio.txt","r") as fd:
	print(fd.read())

with open("mydata.txt","a") as fd:
	fd.write("This is write operation using with")

#Copy the content of file to another file
with open("mybio.txt","r") as fd_1:
	with open("mydata.txt","w") as fd_2:
		fd_2.write(fd_1.read())
