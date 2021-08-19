states = ("MH","MP","DL","CH","UP","JK")

names = []

name = input("Enter your name")
while True:
	state = input("Enter your state")
	if state not in states:
		print("Wrong state name")
	else:
		break
names.append([name,state])



