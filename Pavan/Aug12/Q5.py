al_count={}

giv_string="A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware, operating system main software, and peripheral equipment needed and used for fulloperation. This term may also refer to a group of computers that are linked and function together"
alpha="abcdefghijklmnopqrstuvwxyz"



for i in alpha:
	c=0
	for j in giv_string.lower():
		if i == j:
			c=c+1
	al_count[i]=c
	
for i in al_count.keys():
	print(f"{i} {al_count[i]}")
