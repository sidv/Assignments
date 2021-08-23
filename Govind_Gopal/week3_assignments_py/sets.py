string1 = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

string2 = "A broad range of industrial and consumer products use computers as control systems. Simple special-purpose devices like microwave ovens and remote controls are included, as are factory devices like industrial robots and computer-aided design, as well as general-purpose devices like personal computers and mobile devices like smartphones. Computers power the Internet, which links hundreds of millions of other computers and users. "

txt1 = string1.split(" ")
txt2 = string2.split(" ")
set1 = set(txt1)
set2 = set(txt2)
print ("The common words are")
print (set1.intersection(set2))

print ("Words in set1 not in set2")
print (set1.difference(set2))

print ("Unique words in string 1 are")
print (set1)
print ("Unique words in string 2 are")
print (set2)

set3 = set2.difference(set1)

txt3 = list(txt1)
txt4 = list(set3)
for i in txt4:
	txt3.append(i)
txt5 = " ".join(txt3)
print (txt3)
