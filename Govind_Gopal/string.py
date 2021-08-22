string="Click Open link on the dialog shown by your browser"

print (string[-7:])

print (string[11:15])

print (string.upper())

cli = string[11:15].upper()
str1= string[:11]
str2= string[15:]

print (str1 + cli + str2)

op = string[6:10].upper()
bro = string[-7:].upper()
str1= string[:6]
str2= string[10:44]
print  (str1 + op +str2 + bro)

re = string[6:15]
print ("Open link")
str1 = string[:5]
str2 = string[15:]
print (str1 + " " + re[::-1] + str2)

num = "1,2,3,4,5,6,7,8,9"
print (num[::2])

print (num[2:16:4])
num1 = int(num[:1])
num2 = int(num[8:9])
print (num1 + num2 )

num1 = int(num[2:3])
num2 = int(num[-3:-2])
print (num1 + num2 )
