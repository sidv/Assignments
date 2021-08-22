rng =int(input("Enter the dictionary range"))

dict = {}
o = 0
for i in range(1,rng):
	o += 1
	o = o**2
	dict[i] = o
print (dict)
