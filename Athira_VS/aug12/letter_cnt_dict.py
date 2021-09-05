string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"


n = len(string)
str_dict = {}
for i in range(n):
    if string[i] in str_dict.keys():
        str_dict[string[i]] = str_dict[string[i]]+1
    else:
        str_dict[string[i]] = 1

print(str_dict)
