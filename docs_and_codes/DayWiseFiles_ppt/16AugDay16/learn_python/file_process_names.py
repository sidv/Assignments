"""
with open("names.txt","r") as fd:
	while True:
		line = fd.readline()
		if not line:
			break;
		if line == "Govind\n":
			x=fd.tell()
			print(x)
			with open("names.txt","ab") as fda:
				print(x-len("Govind"))
				fda.seek(x - len("Govind"))
				print(fda.tell())
				fda.write(b"Govind Gopal")
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

with open("names.txt","r+") as fd:
	print(fd.read())
	fd.write("Pavan")
"""




