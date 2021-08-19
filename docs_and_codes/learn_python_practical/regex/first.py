import re #Module for regular expression

string = """A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically.
 Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range
 of tasks. A computer system is a "complete" computer that includes the hardware, operating system (main software), and peripheral
 equipment needed and used for "full" operation. This term may also refer to a group of computers that are linked and function
 together, such as a computer network or computer cluster.

A broad range of industrial and consumer products use computers as control systems. Simple special-purpose devices like microwave
 ovens and remote controls are included, as are factory devices like industrial robots and computer-aided design, as well as 
general-purpose devices like personal computers and mobile devices like smartphones. Computers power the Internet, which links 
hundreds of millions of other computers and users. """

#Findall function
lst = re.findall('i.d.*ial',string) #findall(pattern,string)
print(lst)

#Search functions
#search(pattern,string)
m = re.search(' s.s.*m ',string)
print(m)
print(dir(m))
print(m.span())
print(m.start())
print(m.end())
print(string[m.start():m.end()])
print(m.groups())


#Sub function
#sub(pattern,replace_string,string)
#Returns changed string #not changing the actual string
ret = re.sub("co.{3}ter","xyz",string)
print(ret)

print("______________________________________-")
#split()
#split(pattern,string)
ret = re.split('system',string)
print(ret)














