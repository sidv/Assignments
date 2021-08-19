string = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software and peripheral
equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

lst = string.split(" ")
print(lst)

print(list(filter( lambda x: x != "" and x[0]=='c' and x[-1] == 'r',lst)))


lst_upper = list(map(lambda a: a.upper(),lst[::2] ))
lst_lower = lst[1::2]
print(lst_upper)
print(lst_lower)
indx=0
for i in range(1,2*len(lst_upper),2):
	lst_upper.insert(i,lst_lower[indx])
	indx+=1
print(' '.join(lst_upper))
