

l=[]
for i in range(10,51):
	l.append(i)
print(l)

li=list(map(lambda a:a*a,l))
print(li)


la=list(filter(lambda a:a%2==0,l))
print(la)


s=["sidhant","Pavan","Ramya","Raja"]
s=list(map(lambda a:a[:3],s))
print(s)


str="A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware, operating system main software, and peripheral equipment needed and used for fulloperation. This term may also refer to a group of computers that are linked and function together"
stri=str[::1]
s=list(filter(lambda a:a.upper(),stri))
print(s)


ts=list(filter(lambda a:a.remove(),stri))
print(ts)

#tss=list(filter(lambda a:a[1]==c and s[-1]==r))
#print(tss)

#f=list(map(lambda a:cat))
