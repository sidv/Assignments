#5.Write a python which converts first letter of each word to upper case in above string and print whole string on terminal
string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"


print(string.title())


s = string.split(" ")
x = []
for i in s: 
    if (string.count(i)>=1 and (i not in x)):
        x.append(i)
y = (' '.join(x))
z=y.title()
print(z)
