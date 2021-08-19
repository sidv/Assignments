string1 = "Click Open link on the dialog shown by your browser"

print("1 .fetch browser")
print(string1[-7:])

print("-------------------------------")

print("2 .fetch link")

print(string1[11:16])

print("-------------------------------")
print("3.Convert Whole string to uppercase")

print(string1.upper())

print("-------------------------------")
print("4.Convert whole string to lowercase")

print(string1.lower())

print("-------------------------------")
print("5.Convert Click to upper case in string")
print(string1[:5].upper() + string1[5:])

print("-------------------------------")
print("6.Convert Open and browser to upper case in string")
print(string1[0:6] + string1[6:10].upper() + string1[10:-7]  + string1[-7:].upper())

print("-------------------------------")
print("7.Print Open link: in reverse order")
rev = string1[6:16]
print(rev[::-1])

print("-------------------------------")
num="1,2,3,4,5,6,7,8,9"

print("1.Print only numbers not comma")
print(num[::2])

print("-------------------------------")
print("2.Print all even numbers")

print(num[2::4])

print("-------------------------------")
print("3.Fetch 1 and 5 from string and perform numerical addition")

print(int(num[8]) +  int(num[0]))

print("-------------------------------")
print("4.Fetch 2 and 8from string and perfrom numerical muliplication")


print(int(num[2]) *  int(num[-3]))

print("----------------------------")
