string = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

lst = string.split(" ")
print(lst)

#4.Write a program to convert each alternate index word to upper case in above string. 
print("----alt-----")
alt=list(filter(lambda a: lst.index(a)%2 == 0,lst))
print(alt)
upper = list(map(lambda a: a.upper(),alt))
print(upper)
print(" ".join(upper))

#5.Write a program to convert remove alternate index word from above string.
print("----remove alt------")
notalt=list(filter(lambda a: lst.index(a)%2 != 0,lst))
print(" ".join(notalt))
