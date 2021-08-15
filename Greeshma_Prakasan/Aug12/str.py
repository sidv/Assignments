s = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a computer that includes the hardware, operating system main software, and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"

s = s.replace(" ","").replace(".","").replace(",","")
#print(s)
a=0
si=0
d=0
f=0
for i in s.lower():
	if i=="a":
		a+=1
	elif i=="s":
		si+=1
	elif i=="d":
		d+=1
	elif i=="f":
		f+=1

dic = {}
dic["a"] = a
dic["s"] = si
dic["d"] = d
dic["f"] = f
print(dic)
