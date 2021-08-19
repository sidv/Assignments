string = "Click Open link on the dialog shown by your browser"
num="1,2,3,4,5,6,7,8,9"

print("_______________________________Strings________________________________")
fetchbrowser = string[-7:]
print("Fetch Browser : ", fetchbrowser)
link = string[11:15]
print("Fetch link : ",link)
print("Upper : ", string.upper())
print("Lower is : ", string.lower())

print("Convert Click to Upper case in string:")
print(string[:5].upper() + string[5:])

print("Convert Open and browser to uppercase:")
print(string[:7] + string[7:11].upper() + string[11:-7] + string[-7:].upper())
print("Open link in reverse order :")
print(string[:6] + string[14:5:-1] + string[15:])

print("_______________________________Numbers________________________________")
print("Number without comma")
print[::2]
print("Even Numbers")
print(num[2::4])
print("Fetch 1 and 5 from string and add it")
print(int(num[0]) + int(num[8]))
print("Fetch 2 and 8 from string and multiply it")
print(int(num[2]) * int(num[14]))
