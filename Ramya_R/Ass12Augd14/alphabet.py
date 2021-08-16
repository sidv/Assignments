x="A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware, operating system main software, and peripheral equipment needed and used for fulloperation. This term may also refer to a group of computers that are linked and function together"

a = {}
  
for i in x:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1

print(a)

print("---------------")
for keys in x:
    a[keys] = a.get(keys, 0) + 1
  
print(str(a))
