string = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

#alt upper case
print("___________QN4__________________")
print([x.upper() for x in (string.split(" ")[0::2])])

#remove alt
print("____________QN5_______________")
print([x for x in (string.split(" ")[1::2])])

#start with c and end with r
print("_____________QN6_______________")
print([x for x in (string.split(" ")) if x!="" and x[0]=='c' and x[-1] == 'r'])

#reverse all words
print("___________QN7_________________")
print([x[::-1] for x in(string.split(" "))])

#first letter from words no repeat
print("_____________QN8________________")
print({x[0] for x in (string.split(" ")) if x!=""})
