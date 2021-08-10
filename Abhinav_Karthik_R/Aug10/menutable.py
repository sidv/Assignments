print("_________________Menu Driven Multiplication Table __________________")

while True:
	exit = input("Enter q for exit or press enter to continue")
	if(exit == "q"):
		break
	num = int(input("Enter a number"))
	range = int(input("Enter a range"))
	count = 1
	while(count<=range):
		print(count," x ",num," = " ,num*count)
		count+=1



