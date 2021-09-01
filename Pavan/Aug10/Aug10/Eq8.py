var = "Click Open link on the  dialogue shown by your browser"

while True:

	sub_string=input("Enter your desired substring:\n")
	
	if sub_string.lower() in var.lower():
		print("Yes "+sub_string+" exists in the string.")
