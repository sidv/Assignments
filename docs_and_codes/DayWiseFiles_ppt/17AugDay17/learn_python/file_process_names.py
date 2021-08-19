"""
with open("names.txt","r") as fd:
	while True:
		line = fd.readline()
		if not line:
			break;
		if line == "Govind\n":
			x=fd.tell()
			print(x)
			with open("names.txt","a+b") as fda:
				print(x-len("Govind"))
				fda.seek(x - len("Govind"),0)
				print(fda.tell())
				fda.write(b"Govind Gopal")
"""
"""
with open("names.txt","r") as fd:
	lst = fd.readlines()
	print(lst)
	indx = lst.index("Govind\n")
	lst[indx] = "Govind Gopal\n"
	print(lst)
	with open("names.txt","w") as fdw:
		fdw.writelines(lst)
"""

with open("names.txt","rb+") as fd:
	while True:
		i = fd.readline()
		if not i:
			break;
		print(i)
		if i == b'Govind\n':
			fd.seek((-1)*len("Govind"),1)
			print(fd.tell())
			fd.write(b"Govind Gopal")

#+ extra operation
# r+ -> read write Here + write is not going to truncate the file
# w+ ->read write #Here it is going to truncate



