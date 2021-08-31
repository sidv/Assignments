string = '''A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically.
 Modern computers can perform generic sets of operations known as programs. These programs enable computersto perform a wide range of tasks.
 A computer system is a complete computer that includes the hardware operating system main software and peripheral equipment needed and used
 for full operation. This term may also refer to a group of computers that are linked and function together'''

f = open('data3.txt', 'w')
f.write(string)
f1 = open('data4.txt', 'w')
f1.write(string)
f2 = open('data5.txt', 'w')
f2.write(string)
f3 = open('data6.txt', 'w')
f3.write(string)
f4 = open('data7.txt', 'w')
f4.write(string)
f5 = open('data8.txt', 'w')
f5.write(string)
f6 = open('data9.txt', 'w')
f6.write(string)
f7 = open('data10.txt', 'w')
f7.write(string)
f8 = open('data11.txt', 'w')
f8.write(string)
f9 = open('data12.txt', 'w')
f9.write(string)
f10 = open('data13.txt', 'w')
f10.write(string)
def close(li):
    li.close()

file = [f, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
close(file)
