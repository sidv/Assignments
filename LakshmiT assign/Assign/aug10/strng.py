string="Click Open link on the dialog shown by your browser"
browser=string[-7:]
print(browser)
link=string[11:15]
print(link)
print(string.upper())
print(string.lower())
click=string[:5]
print(click.upper()+ string[5:])
open=string[6:10]
print(string[:6]+string[6:10].upper()+string[10:-7]+string[-7:].upper())
print(string[14:5:-1])


num="1,2,3,4,5,6,7,8,9"
print(num[::2])
print(num[2::4])
num1=int(num[0])
num2=int(num[8])
print(num1+num2)
num1=int(num[2])
num2=int(num[-3])
print(num1*num2)
