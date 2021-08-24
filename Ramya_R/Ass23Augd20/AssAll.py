lst=[]
for i in range(10,51):
	#print(i)
	lst.append(i)
print(lst)

#1. Write a program to generate list of numbers from 10 to 50, Use map to find square of all numbers from list
sq =  [i*i for i in lst if i != 0 ]
print(sq)

#2. Write a program to generate list of numbers from 10 to 50, Use filter to find all even numbers from list
ev =  [i for i in lst if i%2 == 0 ]
print(ev)

#3. Write a code to get first three chars of all strings from list ["Siddhant","Pavan","Ramya","Raja"]
lt = ["Siddhant","Pavan","Ramya","Raja"]
a_lst = [f"{i[0:3]}" for i in lt if i != ""]
print(a_lst)

string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"
str_lst = string.split(" ")

#4.Write a program to convert each alternate index word to upper case in above string. 
print("----alt-----")
#alt_lst = [ele.upper() if str_lst.index[i]%2 == 0 else ele.lower() for i in str_lst]
alt = [i.upper() for i in str_lst[0::2] ]
#alt_lst = [j.lower() if j.isupper() else j.upper() for j in alt]
print(alt)

#5.Write a program to  remove alternate index word from above string.
print("----not alt-----")
no_alt = [i for i in str_lst[1::2] ]
print(no_alt)

#6.Write a program to find all the words from above string where first letter of word is 'c' and last letter is 'r'
print("----------start with c end with r-------")
cr = [i for i in str_lst if i !="" and i[0] =='c' and i[-1] == 'r' ] 
print(cr)

#7.Write a program to reverse all the words of above string
print("----------reverse each word-------")
rev = [i[::-1] for i in str_lst if i !="" ] 
print(rev)

#8.Write a program to find all the first letter of words from above string (No repetition of letters)
print("----------first letter of word-------")
s = {i[0] for i in str_lst if i != "" and i != "\n"}
print(s)










