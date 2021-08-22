str = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computersto perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"
a = 0
o = 0
g = 0
for i in str:
	if i == "a":
		a += 1
	elif i == "s":
		o += 1
	elif i == "d":
		g += 1

print (f"The occurance of 'a' is {a}")
print (f"The occurance of 's' is {o}")
print (f"The occurance of 'd' is {g}")

