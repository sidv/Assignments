states = ("MH","MP","DL","CH","UP","JK","AP")
names = []

name = input("Enter your name: ")
#while True:
for i in states:
	state = input("Enter your state: ")
	if state in states:
		print(state," state name is present")
	else:
		break
names.append([name,state])
print("------------------------------")

#states=()
#state=input("Enter state: ")
#states.append(state)
for i in states:
	print(states)
	break
