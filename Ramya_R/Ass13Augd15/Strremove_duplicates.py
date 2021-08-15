string1 = input("enter string: ")

s = string1.split(" ")
#print(s)
x = []
for i in s:
 
    if (string1.count(i)>=1 and (i not in x)):
        x.append(i)
print(' '.join(x))
