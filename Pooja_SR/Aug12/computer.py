#Write a code to iterate through the given string and store the alphabet and count in dictionary
#-{a:1, s:10, d:20 ,f:30}
x="A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically.Modern computers can perform generic sets of operations known as programs. These programs enable computersto perform a wide range of tasks. A computer system is a complete computerthat includes the hardware operating system main software  and peripheralequipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"
a=0
s=0
d=0
f=0
dic={}
for i in x:
	if i =="a":
		a=a+1
	if i=="s":
		s=s+1
	if i=="d":
		d=d+1
	if i=="f":
		f=f+1
dic["a"]=a
dic["s"]=s
dic["d"]=d
dic["f"]=f
print(dic)
