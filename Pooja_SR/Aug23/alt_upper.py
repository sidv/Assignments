string = '''A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. 
Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks.
 A computer system is a complete computer that includes the hardware operating system main software and peripheral equipment needed and used
 for full operation. This term may also refer to a group of computers that are linked and function together'''


# 4) Write a program to convert each alternate index word to upper case in above string. 

print([x.upper() for x in string.split(" ")[::2]])

print("________________________________________________________")



#print("__________________________")
#print([f"{i[::2].upper()}{i[1:]}" for i in string.split(" ")])
