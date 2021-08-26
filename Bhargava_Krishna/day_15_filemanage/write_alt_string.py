string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer  to a group of computers that are linked and function together"


fd = open("data2.txt", "w")
#fd1 = open("data2.txt","r")

x = string.split(" ")[::2]
y = " ".join(x)
print(y)
fd.write(y)

fd1 = open("data2.txt","r")
print(fd1.read())

fd.close()
fd1.close()
