lst = [["a","b"],["c","d"],["e","f"]]

i=0
o=0
name = input("enter the character to find")

#for i in lst:
#	print (type(i))
#	if type(i) is list:
#		for o in i:
#			if o == name:
#				print (i)
#	else:
#		print ("nothing")

for i in lst:
	if i[o] == name:
		print (i)
	else:
		o += 1
	

