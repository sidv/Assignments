string = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

lst = string.split(" ")
lword = lst[0]
cap = []
for i in lst:
    cap.append(i.capitalize())
    if len(i) > len(lword):
        lword = i
print("_____________________Largest word in string _______________________")
print("largest word is  \n" , lword)
print("_____________________converts first letter of each word to upper case____________")
s = " "
print("First letter capitalized \n" , s.join(cap))
print("______________sort by word________________________")
fil_list = []
for i in lst:
    if "\n" in i :
        i = i.replace("\n","")
        fil_list.append(i)
    else:
        fil_list.append(i)
print("sorted string is  \n",s.join(sorted(fil_list)))

print("___________________lower to upper and vice versa __________________")
s = ""
for i in string:
    if i.islower():
        s = s + i.upper()
    elif i.isupper():
        s = s + i.lower()
    else:
        s = s + i
print(s)