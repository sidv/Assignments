#5.Write a code to iterate through the given string and store the alphabet and count in dictionary
#-{a:1, s:10, d:20 ,f:30}
#"A computer is a machine that can be programmed to carry out sequences of
# arithmetic or logical operations automatically. Modern computers can perform
# generic sets of operations known as programs. These programs enable computers
# to perform a wide range of tasks. A computer system is a complete computer
# that includes the hardware operating system main software  and peripheral
# equipment needed and used for full operation. This term may also refer 
#to a group of computers that are linked and function together"


string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs.These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"

dictalp = {} # Empty String

for i in string:
	if (i != '.' and i != ' '):
		dictalp[i] = string.count(i)

print("______Dictionary Alphabet_______")
print(dictalp)
