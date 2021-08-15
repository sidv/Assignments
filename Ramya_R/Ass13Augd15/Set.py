
string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"

string2 = "A broad range of industrial and consumer products use computers as control systems. Simple special-purpose devices like microwave ovens and remote controls are included, as are factory devices like industrial robots and computer-aided design, as well as general-purpose devices like personal computers and mobile devices like smartphones. Computers power the Internet, which links hundreds of millions of other computers and users. "

s1=set(string.split(" "))
s2=set(string2.split(" "))

#9.Write a program to find all the common words in above string and string2
print("common words-----------------")
s=s1.intersection(s2)
print(' '.join(s))
#10.Write a program to find all the words available in above string but not available in string2
print("all words available in 1st string not in str2")
x=s1.difference(s2)
print(' '.join(x))

#11.Write a program to find all the unique words in above string and string2
print("---unique words-------")
y=s1.symmetric_difference(s2)
print(' '.join(y))
a=s1.union(s2)
b=a.difference(s)
print(' '.join(b))

#12.Write a progran to append all words from above string2 to string if they are not in string
print("---append all words  of string2 to string-----")
z=s1.union(s2.difference(s1))
print(' '.join(z))


