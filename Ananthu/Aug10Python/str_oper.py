string = "Click Open link on the dialog shown by your browser"
print(string)
print("-----------------------------------------------------")

print("1.Fetching 'browser'")
print("------------------")
print(string[44:])

print("2.Fetching 'link'")
print(string[11:15])

print("3.Converting whole string to 'UPPERCASE'")
print(string.upper())

print("4.Converting whole string to 'lowercase'")
print(string.lower())

print("5.'click' to UPPERCASE")
a=string[:5]
print(a.upper() + string[5:])

print("6.'open' and 'browser' to uppercase")

x = string[6:10].upper()
y = string[44:].upper()
print(string[:6] + x + string[10:44] + y)

print("7.'open link' in reverse order")

rev = string[14:5:-1]
print(string[:6] + rev + string[15:])


print("----------------------------- PART 2 --------------------------------------------")

num = "1,2,3,4,5,6,7,8,9"

print(num[::2])

print(num[2::4])

a = num[0]
b = num[8]
add = int(a)+int(b)
print(add)

p = num[2]
q = num[14]
print(int(p) * int(q))
