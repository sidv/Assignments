a="Click Open link on the dialog shown by your browser"
  #0123456789123456789123456789123456789123456789123456

print(a[-7:])
print(a[11:16])
print(a.upper())
print(a.lower())
print(a[0:5].upper())
j=a[0:5].upper()
l=j+a[5:]
print(l)


b=a[-7:].upper()
c=a[6:10].upper()
d=c+" "+b
print(d)
print(a[0:6]+c+a[10:-7]+b)

print(a[-37:5:-1])


num="1,2,3,4,5,6,7,8,9"
x=num[0::2]
print("only num without ,-----")
print(x)
#odd num
y=x[0::2]
print("odd------")
print(y)
#even num
z=x[1::2]
print("even-----")
print(z)
#fetch 1,5
k=y[0:4:2]
print("fetch 1 & 5----")
print(k)
print("addition-----")
print(int(k[0])+int(k[1]))
#fetch 2 & 8
v=z[0::3]
print("fetch 2 $ 8-----")
print(v)
print("multip------")
print(int(v[0])*int(v[1]))
