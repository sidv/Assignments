string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"
str_lst = string.split(" ")

#4.Write a program to convert each alternate index word to upper case in above string. 
print("_______________________________alternate_______________________________")
altr = [i.upper() for i in str_lst[0::2] ]
print(altr)

#5.Write a program to  remove alternate index word from above string.
print("___________________alternate index word_____________________")
altr_index = [i for i in str_lst[1::2] ]
print(altr_index)

#6.Write a program to find all the words from above string where first letter of word is 'c' and last letter is 'r'
print("____________________word starts with c ends with r_________________________")
word = [i for i in str_lst if i !="" and i[0] =='c' and i[-1] == 'r' ] 
print(word)

#7.Write a program to reverse all the words of above string
print("____________________reverse all words__________________")
revrs = [i[::-1] for i in str_lst if i !="" ] 
print(revrs)
