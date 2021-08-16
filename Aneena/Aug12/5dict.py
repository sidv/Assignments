str = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks.A computer system is a complete computer that includes the hardware operating system main software and peripheral equipment needed and used for full operation.This term may also refer to a group of computers that are linked and function together"

a=0
s=0
d=0
f=0
dict={}
for i in str:
	if i=="a":
		a=a+1
	if i=="s":
		s=s+1
	if i=="d":
		d=d+1
	if i=="f":
		f=f+1
dict["a"]=a
dict["s"]=s
dict["d"]=d
dict["f"]=f
print(dict)
