str="Click open link  on the  dialog shown byyour browser"

print("Fetch browser : " ,str[-7:])
print("Fetch link : " ,str[11:16])
print("whole string in upper : " ,str.upper())
print("whole string in lower : ",str.lower())
print("Click to upper : ", str[:5].upper() + str[5:])
print("open  and browser to upper : ", str[:6] + str[6:10].upper() + str[10:44] + str[-7:].upper())
print("open link in reverse order : ",str[15:5:-1])

