states=("MH","MD","DL","KL","CH")

names=[]

name=input("enter state name")
while True:
	state=input("enter your state")

	if state not in states:
		print("wrong state name")
	else:
		break
names.append([name,state])
print(names)

