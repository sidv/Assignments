string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer  to a group of computers that are linked and function together"


ls_upper = list(map(lambda a : a.upper(), string[::2]))
ls_lower = string[1::2]
print(ls_upper)
print(ls_lower)
indx = 0
for i in range(1,2*len(ls_upper),2):
	ls_upper.insert(i,ls_lower[indx])
	indx+=1
	
print(" ".join(ls_upper))
