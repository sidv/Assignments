string1 = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software  and peripheral
equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

lst = string1.split(" ")

print("___________Qn4_______________________")

x = list(filter(lambda x : lst.index(x)%2 == 0 , lst))
upper = list(map(lambda x : x.upper(), x))
print(" ".join(upper))

print("____________Qn5_____________________")

xalt = list(filter(lambda x : lst.index(x)%2 !=0 , lst))
print(" ".join(xalt))

print("_____________Qn6____________________")

cr = list(filter(lambda x : x != "" and (x[0] == "c" and x[-1] == "r") , lst))
print(cr)

print("_________________Qn7__________________")

rv = list(map(lambda x : x[::-1],lst))
print(" ".join(rv))

print("__________________Qn8__________________")

fl = list(filter(lambda x : x != "" , lst))
print(set(map(lambda x : x[0],fl)))

#print("__________________string into file data1.txt____________________")

fd = open("data1.txt","w")
fd.write(string1)
fd.close()

#print("__________alternate index words in to the file data2.txt___________")

fd = open("data2.txt","w")
fd.write(" ".join(x))
fd.close()

print("_______find all the words in data1.txt but not in data2.txt__________")

fd1 = open("data1.txt","r")
fd2 = open("data2.txt","r")
a = set(fd1.read().split(" "))
b = set(fd2.read().split(" "))
print(a.difference(b))
fd1.close()
fd2.close()

#print("_______write string in 10 files_________")

for i in range(3,14):
    fd = open(f"data{i}.txt","w")
    fd.write(string1)
    fd.close()