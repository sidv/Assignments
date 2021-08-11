s = "Click Open link on the dialog shown by your browser"
    
b = s[44:]
print(b)

l = s[11:16]
print(l)

u = s.upper()
print(u)

l = s.lower()
print(l)

c = s[:6].upper()
print(c+s[6:])

B = b.upper()
o = s[6:11].upper()
print(s[:6]+o+s[11:44]+B)

sub = s[14:5:-1]
print(sub)
 

num = "1,2,3,4,5,6,7,8,9"
print(num[0:17:2])
print(num[::2])

print(num[2:17:4])
print(num[2::4])

print(int(num[0]) + int(num[8]))

print(int(num[2]) * int(num[14]))

n = num[0:17:2]

print(int(n[0]) + int(n[7]))


