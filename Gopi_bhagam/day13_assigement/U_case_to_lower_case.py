
string="""A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""


print("**************lower to upper*****************")
output=""
for ch in string:
    if ord(ch)>=ord('a') and ord(ch)<=ord('z'):
        ch=chr(ord(ch)-32)
        output=output+ch
print(output)



print("**************upper to lower*****************")
output=""
for ch in string:
    if ord(ch)>=ord('A') and ord(ch)<=ord('Z'):
        ch=chr(ord(ch)+32)
        output=output+ch
print(output)















