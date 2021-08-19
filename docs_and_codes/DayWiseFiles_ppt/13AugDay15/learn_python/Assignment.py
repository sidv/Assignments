var = "Click Open link on the dialog shown by your browser"

print(var[-7:])
print(var[12:16])
print(var.upper())
print(var.lower())

x=var[:5].upper() + var[5:]
print(x)

#var[:7] Click
#var[7:11].upper() OPEN
#var[11:-7] link .... your 
#var[-7:].upper() BROWSER

x =var[:7] + var[7:11].upper() + var[11:-7] + var[-7:].upper()
print(x)

print(var[16:7:-1])
    #012345678
num="1,2,3,4,5,6,7,8,9"
print(num[::2])
print(num[2::4])
res = int(num[0]) + int(num[8])
