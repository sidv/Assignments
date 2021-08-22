#11.Write the above string alternate index words into the file data2.txt

string1 = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software  and peripheral
equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

lst = string1.split(" ")

data = list(map(lambda a: a,list((filter(lambda a: lst.index(a)%2 == 0, lst)))))
data = str(data)

with open('data2.txt', 'w') as file:
  file.write(data)