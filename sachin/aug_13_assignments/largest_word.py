#4.Write a python code to find the largest word in below multiline string.


string = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software  and peripheral
equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""
m_len = -1
lst = string.split(" ")
for i in lst:
    if len(i) > m_len:
        m_len = len(i)
        result = i

print("largest word is : " + result)