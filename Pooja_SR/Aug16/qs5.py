string = '''A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. 
Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks.
 A computer system is a complete computer that includes the hardware operating system main software and peripheral equipment needed and used
 for full operation. This term may also refer to a group of computers that are linked and function together'''

#print(list(map(lambda a: a[::2].remove(), string)))

print("___________________________________________________________________________")
x = string.split(" ")
lst = []
for i in x:
    if i[0] == 'c' and i[-1] == 'r':
        lst.append(i)
print(set(lst))
