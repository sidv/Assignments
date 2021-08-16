x="click open link on the dialog shown by your browser"
#1fetch browser
print(x[44:])
#2fetch link
print(x[11:15])
#3convert whole string to uppercase
print(x.upper())
#4conver string to lowercase
print(x.lower())
#5conver click to uppercase in string
first=x[:6]
other=x[6:]
z=first.upper()
x=z+other
print(x)
#6convert open and browser to upper case
a=x[44:]
b=x[6:10]
d=a.upper()
e=b.upper()
print(x[:6]+b+x[10:44]+d)
#7print open link in reverse order
print(x[14:5:-1])
