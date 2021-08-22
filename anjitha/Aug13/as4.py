
str='''A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform 
generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that
 includes the hardware, operating system main software, and peripheral equipment needed and used for fulloperation. This term may also refer to a group of 
computers that are linked and function together'''

stri=str.replace(".","").replace(",","")
#print(stri)
new=stri.split(" ")
print(new)
l=new[0]
for i in new:
	if len(i) > len(l):
		l=i
print(l)
	

