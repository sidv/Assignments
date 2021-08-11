string = "Click Open link on the dialog shown by your browser"

sttr1 = input("Enter substring")

while True:
	if sttr1 in string:
		print("Substring found")
		break
	else:
		print("Not found")
		break
