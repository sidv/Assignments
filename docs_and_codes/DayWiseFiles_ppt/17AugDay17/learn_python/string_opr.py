data = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software  and peripheral
equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

#For multiline string use triple quotes
data1 = "1:2:3:4:5:6"
data2 = "1,2,3,4,5,6,7,8,9"

#print(list(data))
lst = data.split(" ") #splits based on seperator It returns list
print(lst)
print("|".join(lst)) #You can pass list as a argument. Joines based on seperator and creates a string

lst = data1.split(":")
print(lst)
print("#".join(lst))

lst = data2.split(",")
print(lst)
print("=>".join(lst))

name = "Siddhant"
print("|".join(name))

words = {}
for i in data.split(" "):
	if i not in words.keys():
		words[i] = lst.count(i)

print(words)




