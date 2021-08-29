string = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
 to a group of computers that are linked and function together"""

lst = string.split(" ")
a = list(filter(lambda a: lst.index(a)%2 == 0,lst))
upper =  list(map(lambda b: b.upper(),a))
print(upper)
"""
res = ""
for i in range(len(string)):
	if not  i%2:
		res = res + string[i].upper()
	else:
		res = res + string[i].lower()
print("___Alternate letters in uppercase___:\n"+str(res))
"""
