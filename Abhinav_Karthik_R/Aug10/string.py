s = "Click open link on the dialog shown by your browser"

print("Fetch browser : " ,s[-7:])
print("Fetch link : " ,s[11:16])
print("whole string in upper : " ,s.upper())
print("whole string in lower : ",s.lower())
print("Click to upper : ", s[:5].upper() + s[5:])
print("open  and browser to upper : ", s[:6] + s[6:10].upper() + s[10:44] + s[-7:].upper())
print("open link in reverse order : ",s[15:5:-1])
