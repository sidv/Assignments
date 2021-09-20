# 4 Write a python code to find the largest word in below multiline string. 

string2 = """A broad range of industrial and consumer products use computers as control systems. Simple special-purpose devices like microwave ovens and remote controls are included, as are factory devices like industrial robots and computer-aided design, as well as general-purpose devices like personal computers and mobile devices like smartphones. Computers power the Internet, which links hundreds of millions of other computers and users."""
stri=string2.replace(".","").replace(",","")
new=stri.split(" ")
#print(new)
l=new[0]
for i in new:
	if len(i) > len(l):
		l=i
print(l)
