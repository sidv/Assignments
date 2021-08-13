#Store all the states name in tuple.And iterate through it and print on terminal 
states = ("kerala","Tamilnadu","Karnataka")
while True:
	state = input("Enter your state")
	if state  in states:
		print("ya its found")
	else:   print("not found")
	break;
