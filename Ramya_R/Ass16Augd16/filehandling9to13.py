string = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""
lst = string.split(" ")

#10.Write the above string into file data1.txt
print("------write string in data1.txt-----")
fd = open("data1.txt","w")
fd.write(string)
fd.close()

#11.Write the above string alternate index words into the file data2.txt
print("------alt words in string copy to data2 -----")
alt=list(filter(lambda a: lst.index(a)%2 == 0,lst))
fd = open("data2.txt","w")
fd.write(" ".join(alt))
fd.close()

#12.Write the code to find all the words in data1.txt but not in data2.txt
print("------diff b/w data1 and data2-----")
fd1 = open("data1.txt","r")
fd2 = open("data2.txt","r")
a = set(fd1.read().split(" "))
b = set(fd2.read().split(" "))
print(a.difference(b))
fd1.close()
fd2.close()

#13.Write the above string into 10 files data3.txt,data4.txt and so on..
print("------write string in 10 files-----")
for i in range(3,14):
	fd = open(f"data{i}.txt","w")
	fd.write(string)
	fd.close()


