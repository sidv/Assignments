q_string= "Click Open link on the dialog shown by your browser"

res = q_string.split()

for i in res:
	if(i=="browser" or i=="link"):
		print(i)
print(q_string.upper())
print(q_string.lower())
print(res[0].upper())
print(res[1].upper(),res[2].upper())
print(res[2],res[1])
