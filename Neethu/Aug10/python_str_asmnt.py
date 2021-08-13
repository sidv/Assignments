x="click open link on the dialog shown by your browser"


#fetch browser

first =x[44:]
#fetch link
other = x[11:15]
print(first)
print(other)

# convert string to upper
z=x[:-1].upper()
print(z)

#convert string to lower
y=x[:-1].lower()
print(y)

# conver "open" and "browser" to uppercse in string
x="open browser"
upper=x.upper()
print(upper)

# print "open link: in reverse order"

print(x[16:7:-1])


#print  only number not comma

num="1,2,3,4,5,6,7,8,9"
print(num[::2])

#print all even numbers
print(num[2::4])
#fetch "1" and "5" from string and perform numerical addition


a=num[0]
b= num[8]
res=int(a)+int(b)
print(int(a)+int(b))
#fetch "2" and "8" from string and perform numerical multiplication
c=num[2]
d=num[14]
print(int(c)*int(d))

