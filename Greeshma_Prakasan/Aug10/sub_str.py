s = "Click Open link on the dialog shown by your browser"

sub = input("enter the sub string : ")

while sub.lower() in s.lower():
	print("it is a substring")
	break
	
