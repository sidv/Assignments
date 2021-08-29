string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"
string2 = "A broad range of industrial and consumer products use computers as control systems. Simple special-purpose devices like microwave ovens and remote controls are included, as are factory devices like industrial robots and computer-aided design, as well as general-purpose devices like personal computers and mobile devices like smartphones. Computers power the Internet, which links hundreds of millions of other computers and users. "

string = string.replace(".","").replace(",","")
s1 = string.split(" ")
s1 = set(s1)
string2 = string2.replace(".","").replace(",","").replace("-","")
s2 = string2.split(" ") 
s2 = set(s2)
s = s1 - s2
for i in s:
	string += " "+i
print(string)


