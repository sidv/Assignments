string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"
string2 = "A broad range of industrial and consumer products use computers as control systems. Simple special-purpose devices like microwave ovens and remote controls are included, as are factory devices like industrial robots and computer-aided design, as well as general-purpose devices like personal computers and mobile devices like smartphones. Computers power the Internet, which links hundreds of millions of other computers and users. "


def large_str(string):
	string = string.replace(".","").replace(",","").replace("-","")
	s = string.split(" ")

	l = s[0] 
	for i in s:
		if len(i) > len(l):
			l = i
	print(l)

#large_str(string2)

def str_cap(string):
	s = string.split(" ")
	new = []
	for i in s:
		new.append(i.title())
	new = " ".join(new)
	print(new)

#str_cap(string)

def sort_alpha(string):
	string = string.replace(".","").replace(",","")
	s = string.split(" ")
	s.sort()
	s = " ".join(s)
	print(s)

#sort_alpha(string)

def sort_word(string):
	string = string.replace(".","").replace(",","")
	s = string.split(" ")
	s.sort(key=len)
	s = " ".join(s)   
	print(s)

#sort_word(string)

def str_up_low(string):
	s = ""
	for i in string:
		if i.isupper():
			s += i.lower()
		elif i.islower():
			s += i.upper()
		else:
			s += i
	print(s)

#str_up_low(string)

def common1(string,string2):
	string = string.replace(".","").replace(",","")
	s1 = string.split(" ")
	string2 = string2.replace(".","").replace(",","").replace("-","")
	s2 = string2.split(" ")
	s = set()
	for i in s1:
		for j in s2:
			if i.lower()==j.lower():
				s.add(i)
	for i in s:
		if i.isalnum():
			print(i)

#common1(string,string2)

def common2(string,string2):
	string = string.replace(".","").replace(",","")
	s1 = string.split(" ")
	s1 = set(s1)
	string2 = string2.replace(".","").replace(",","").replace("-","")
	s2 = string2.split(" ") 
	s2 = set(s2)
	s = s1 & s2	#intersection
	for i in s:
		if i.isalnum():
			print(i)

#common2(string,string2)

def str_diff(string,string2):
	string = string.replace(".","").replace(",","")
	s1 = string.split(" ")
	s1 = set(s1)
	string2 = string2.replace(".","").replace(",","").replace("-","")
	s2 = string2.split(" ") 
	s2 = set(s2)
	s = s1 - s2	#difference
	for i in s:
		print(i)

#str_diff(string,string2)

def str_uniq(string,string2):
	string = string.replace(".","").replace(",","")
	s1 = string.split(" ")
	s1 = set(s1)
	string2 = string2.replace(".","").replace(",","").replace("-","")
	s2 = string2.split(" ") 
	s2 = set(s2)
	s = s1 ^ s2	#symmetric difference
	for i in s:
		print(i)

#str_uniq(string,string2)


def append_w(string,string2):
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

append_w(string,string2)
