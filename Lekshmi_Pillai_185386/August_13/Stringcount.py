#7.Write a program which counts the total letters and digits in the string(take string from user)

string = input("Enter the string")
digitcount=0
digitchar=0
for i in string:
	if i.isdigit():
		digitcount +=1
	elif (i == " " or  i == "."):
		pass
	else:
		digitchar+=1
print(f"Digit Count => {digitcount}")
print(f"Total Letters Count => {digitchar}")
		
