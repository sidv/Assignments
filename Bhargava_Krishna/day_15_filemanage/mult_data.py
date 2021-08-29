string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer  to a group of computers that are linked and function together"


count = 3
while count<13:
	f_name = f"data{count}.txt"
	print(f_name)
	
	with open(f_name,"w") as fd:
		fd.write(f_name)
		
	count += 1
