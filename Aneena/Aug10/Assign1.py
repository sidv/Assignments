x= "Click Open link on the dialog shown by your browser"

#1 Fetch browser

print(x[44:51])
#or (x[-7:]

#2 Fetch link

print(x[11:15])
#or [12:16]

#3 convert string to uppercase

print(x.upper())

#4 convert string to lowercase

print(x.lower())

#5 convert click to uppercase in string

#first=x[:5]
#other=x[5:]
#z=first.upper()
#x=z+other
#print(x)

#6 convert open and browser to uppercase in string

a=x[6:10]
b=x[44:51]
c=a.upper()
d=b.upper()
other=x[:5]
other1=x[11:43]
e= other + c + other1 + d
print(e)

# OR
#x[:7] Click
#x[7:11].upper() OPEN
#x[11:-7] link.....your
#x[-7:].upper() BROWSER
#m=x[:7] + x[7:11].upper() + x[11:-7] + x[-7:].upper()
#print(m)



#7. open link in reverse order
print(x[16:7:-1])

