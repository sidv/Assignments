str="Click open link on the dilog shown by your browser"

x=str[43: ]
y=str[11:15]
print(x)
print(y)

print("to upper case:",str.upper())
print("to lower case:",str.lower())

a=str[0:5].upper()+str[6:]
print("click to upper:",a)

upp=x.upper()
print("browser to upper:",upp)

rev=str[14:5:-1]
print("reverse of open link is :",rev)

num="1,2,3,4,5,6,7,8,9"
n1=num[0:17:2]
print("without comma:",n1)

n2=num[2:17:4]
print("even number:",n2)

n3="1,2,3,4,5,6,7,8,9"
x,y=n3[0],n3[8]
print(int(x)+int(y))

