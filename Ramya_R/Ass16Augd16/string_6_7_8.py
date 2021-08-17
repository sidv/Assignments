string = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

lst = string.split(" ")
print(lst)

#6.Write a program to find all the words from above string where first letter of word is 'c' and last letter is 'r'
print("----------start with c end with r-------")
print(list(filter(lambda a: a !="" and a[0] =='c' and a[-1] == 'r',lst)))

#7.Write a program to reverse all the words of above string
print("----------reverse each word-------")
print(list(map(lambda a: a[::-1],lst)))

#8.Write a program to find all the first letter of words from above string (No repetition of letters)
print("----------first letter of word-------")
x= list(filter(lambda a: a != "",lst))
print(set(map(lambda a: a[0],x)))
